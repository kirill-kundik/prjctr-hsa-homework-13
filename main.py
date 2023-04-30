import argparse
import csv
import itertools
import multiprocessing
import time

import faker
import pystalk
import redis

CLIENTS = {"beanstalkd": pystalk.BeanstalkClient(host="beanstalkd", port=11300),
           "redis_rdb": redis.Redis(host="redis_rdb", port=6379, db=0),
           "redis_aof": redis.Redis(host="redis_aof", port=6379, db=0), }

DEFAULT_PRINTING_SIGN = "="


def csv_writer(filename, row, mode="a"):
    with open(filename, mode) as file:
        csv.writer(file).writerow(row)


def printer(text, start=False, end=False):
    if start:
        print()
        print(DEFAULT_PRINTING_SIGN * 110)

    print(DEFAULT_PRINTING_SIGN * 5, end="")
    print(f"{text:^100}", end="")
    print(DEFAULT_PRINTING_SIGN * 5)

    if end:
        print(DEFAULT_PRINTING_SIGN * 110)
        print()


def read(client, n):
    elapsed_times = []
    c = CLIENTS[client]
    beanstalkd = client == "beanstalkd"

    processed = 0

    while processed < n:
        start_time = time.monotonic_ns()

        if beanstalkd:
            job = c.reserve_job()
            c.delete_job(job.job_id)
        else:
            if not c.lpop("queue_data"):
                continue

        elapsed_time = (time.monotonic_ns() - start_time) / 1_000_000
        elapsed_times.append(elapsed_time)

        processed += 1

    return elapsed_times


def push(client, n, fake):
    c = CLIENTS[client]
    beanstalkd = client == "beanstalkd"
    elapsed_times = []

    for _ in range(n):
        data = fake.json()

        start_time = time.monotonic_ns()
        if beanstalkd:
            c.put_job(data)
        else:
            c.rpush("queue_data", data)
        elapsed_time = (time.monotonic_ns() - start_time) / 1_000_000

        elapsed_times.append(elapsed_time)

    return elapsed_times


def run_experiment(processes, func, func_args):
    start_time = time.monotonic_ns()

    with multiprocessing.Pool(processes) as pool:
        results = pool.starmap(func, [func_args for _ in range(processes)])

    total_time = (time.monotonic_ns() - start_time) / 1_000_000

    results = list(itertools.chain.from_iterable(results))
    len_ = len(results)
    return {
        "avg_time": sum(results) / len_,
        "max_time": max(results),
        "min_time": min(results),
        "total_time": total_time,
        "total_messages_sent": len_,
    }


def main(writer=False, reader=False):
    if not any((writer, reader)):
        raise ValueError(f"{writer=} and {reader=}")

    mode = "writer" if writer else "reader"

    fake = faker.Faker()

    messages = [1000, 10000]
    processes = [2, 4, 8, 16]
    delay_between_experiments = 5

    output_file = f"/results/{mode}_{int(time.time())}.csv"
    headers = ["Client", "Processes", "Total messages",
               "Total time (ms)", "Average time (ms)", "Min time (ms)", "Max time (ms)"]
    csv_writer(output_file, headers, mode="w")

    if reader:
        time.sleep(1)

    start_time = time.time()

    for client in sorted(CLIENTS.keys()):
        for p in processes:
            for n in messages:
                text = f"EXPERIMENT FOR {client} CLIENT IN {mode.upper()} MODE " \
                       f"WITH {n} MESSAGES AND {p} PROCESSES"
                printer(text, start=True)

                if reader:
                    func = read
                    func_args = (client, n)
                else:
                    func = push
                    func_args = (client, n, fake)

                res = run_experiment(p, func, func_args)

                total_messages_sent = res["total_messages_sent"]
                total_time = f"{res['total_time']:.3f}"
                avg_time = f"{res['avg_time']:.3f}"
                min_time = f"{res['min_time']:.3f}"
                max_time = f"{res['max_time']:.3f}"

                csv_writer(output_file, [client, p, total_messages_sent, total_time, avg_time, min_time, max_time])

                printer(f"SUCCEED IN {total_time} ms")

                printer(
                    f"Total messages: {total_messages_sent:6d} | "
                    f"Avg Time: {avg_time} ms | "
                    f"Min Time: {min_time} ms | "
                    f"Max Time: {max_time} ms",
                    end=True
                )

                time.sleep(delay_between_experiments)

    print(f"Finished all experiments for {time.time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Queue Reader/Writer",
        description="This program tests different queues performance.",
        epilog="Good luck, have fun!"
    )
    parser.add_argument("--writer", action=argparse.BooleanOptionalAction)
    parser.add_argument("--reader", action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    main(writer=args.writer, reader=args.reader)
