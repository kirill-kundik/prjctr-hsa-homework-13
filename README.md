# PRJCTR Homework 13: Queues 

The task was to set up 3 services which provides queues management: 
[beanstalkd](https://beanstalkd.github.io/) with persistent storage, 
[redis](https://redis.io/docs/management/persistence/) database, and 
redis in append only file mode. Compare and measure queues performance. 

## Prerequisites

* Installed [Docker](https://www.docker.com/products/docker-desktop/).

## Setup

Firstly, execute following command to build required images:

```bash
$ docker-compose build
```

Then run the containers (all performance for writing and reading 
experiments will begin automatically):

```bash
$ docker-compose up -d
```

Results of the experiments will be located in `./results` folder in csv format.

## Results

### Writing

|Client    |Processes|Total messages|Total time (ms)|Average time (ms)|Min time (ms)|Max time (ms)|
|----------|---------|--------------|---------------|-----------------|-------------|-------------|
|beanstalkd|2        |2000          |4866.613       |0.301            |0.094        |5.823        |
|beanstalkd|2        |20000         |48394.747      |0.325            |0.141        |6.603        |
|beanstalkd|4        |4000          |5004.680       |0.349            |0.108        |16.970       |
|beanstalkd|4        |40000         |50593.911      |0.344            |0.099        |18.036       |
|beanstalkd|6        |6000          |5109.711       |0.356            |0.124        |5.621        |
|beanstalkd|6        |60000         |52261.955      |0.361            |0.102        |35.172       |
|beanstalkd|8        |8000          |6475.784       |0.515            |0.110        |36.477       |
|beanstalkd|8        |80000         |60450.301      |0.488            |0.096        |35.494       |
|beanstalkd|10       |10000         |7905.367       |1.226            |0.104        |25.078       |
|beanstalkd|10       |100000        |70891.176      |1.442            |0.094        |37.565       |
|beanstalkd|12       |12000         |8957.996       |2.236            |0.135        |29.052       |
|beanstalkd|12       |120000        |85692.546      |2.521            |0.097        |92.058       |
|beanstalkd|14       |14000         |14096.836      |4.286            |0.140        |102.888      |
|beanstalkd|14       |140000        |106879.384     |3.717            |0.097        |32.231       |
|beanstalkd|16       |16000         |13040.260      |4.262            |0.119        |38.883       |
|beanstalkd|16       |160000        |114535.605     |4.654            |0.098        |60.758       |
|redis_aof |2        |2000          |4790.674       |0.338            |0.194        |6.121        |
|redis_aof |2        |20000         |47815.738      |0.331            |0.149        |8.179        |
|redis_aof |4        |4000          |4873.433       |0.375            |0.221        |13.237       |
|redis_aof |4        |40000         |49464.894      |0.373            |0.148        |37.521       |
|redis_aof |6        |6000          |6325.518       |0.989            |0.169        |20.277       |
|redis_aof |6        |60000         |57040.350      |0.746            |0.157        |41.327       |
|redis_aof |8        |8000          |7951.718       |1.723            |0.210        |32.291       |
|redis_aof |8        |80000         |78179.002      |1.953            |0.153        |40.515       |
|redis_aof |10       |10000         |10179.598      |2.705            |0.164        |42.700       |
|redis_aof |10       |100000        |98190.827      |2.697            |0.170        |37.256       |
|redis_aof |12       |12000         |11119.335      |3.144            |0.169        |26.820       |
|redis_aof |12       |120000        |128028.058     |4.088            |0.180        |47.964       |
|redis_aof |14       |14000         |14349.309      |4.361            |0.173        |35.766       |
|redis_aof |14       |140000        |152176.498     |5.031            |0.184        |48.118       |
|redis_aof |16       |16000         |17193.006      |5.183            |0.179        |71.286       |
|redis_aof |16       |160000        |193749.927     |5.878            |0.197        |90.480       |
|redis_rdb |2        |2000          |4914.542       |0.339            |0.161        |19.875       |
|redis_rdb |2        |20000         |47895.485      |0.322            |0.147        |6.322        |
|redis_rdb |4        |4000          |4819.764       |0.347            |0.147        |6.304        |
|redis_rdb |4        |40000         |49771.027      |0.365            |0.140        |41.206       |
|redis_rdb |6        |6000          |6401.006       |0.774            |0.154        |33.341       |
|redis_rdb |6        |60000         |58512.321      |0.879            |0.146        |41.268       |
|redis_rdb |8        |8000          |10112.544      |2.771            |0.160        |21.425       |
|redis_rdb |8        |80000         |78251.123      |2.002            |0.140        |41.107       |
|redis_rdb |10       |10000         |9184.887       |2.431            |0.147        |29.195       |
|redis_rdb |10       |100000        |89679.262      |2.585            |0.131        |40.979       |
|redis_rdb |12       |12000         |11549.067      |3.656            |0.159        |63.638       |
|redis_rdb |12       |120000        |113289.519     |3.775            |0.132        |42.067       |
|redis_rdb |14       |14000         |13190.196      |4.109            |0.158        |50.618       |
|redis_rdb |14       |140000        |135250.690     |4.758            |0.140        |46.344       |
|redis_rdb |16       |16000         |16254.444      |5.435            |0.172        |46.547       |
|redis_rdb |16       |160000        |160574.450     |5.679            |0.151        |73.046       |


### Reading

|Client    |Processes|Total messages|Total time (ms)|Average time (ms)|Min time (ms)|Max time (ms)|
|----------|---------|--------------|---------------|-----------------|-------------|-------------|
|beanstalkd|2        |2000          |3855.918       |3.793            |0.255        |19.562       |
|beanstalkd|2        |20000         |48397.478      |4.830            |0.209        |17.627       |
|beanstalkd|4        |4000          |5006.693       |4.891            |0.202        |33.464       |
|beanstalkd|4        |40000         |50595.020      |5.027            |0.160        |41.795       |
|beanstalkd|6        |6000          |5110.366       |4.962            |0.206        |29.643       |
|beanstalkd|6        |60000         |52263.085      |5.193            |0.167        |66.968       |
|beanstalkd|8        |8000          |6478.646       |6.205            |0.213        |40.624       |
|beanstalkd|8        |80000         |60452.483      |5.987            |0.162        |60.284       |
|beanstalkd|10       |10000         |7908.097       |7.466            |0.219        |88.320       |
|beanstalkd|10       |100000        |70886.523      |7.007            |0.172        |89.047       |
|beanstalkd|12       |12000         |8962.500       |8.663            |0.225        |49.958       |
|beanstalkd|12       |120000        |85697.470      |8.504            |0.164        |204.737      |
|beanstalkd|14       |14000         |14081.566      |13.754           |0.218        |217.954      |
|beanstalkd|14       |140000        |106899.849     |10.605           |0.177        |89.063       |
|beanstalkd|16       |16000         |13042.079      |12.701           |0.241        |264.012      |
|beanstalkd|16       |160000        |114543.698     |11.367           |0.188        |89.490       |
|redis_aof |2        |2000          |4778.330       |0.274            |0.177        |7.418        |
|redis_aof |2        |20000         |47814.340      |0.264            |0.128        |3.236        |
|redis_aof |4        |4000          |4870.956       |0.363            |0.139        |1.101        |
|redis_aof |4        |40000         |49466.038      |0.373            |0.141        |41.999       |
|redis_aof |6        |6000          |6329.340       |0.532            |0.134        |12.379       |
|redis_aof |6        |60000         |57035.298      |0.594            |0.120        |41.040       |
|redis_aof |8        |8000          |7950.618       |0.730            |0.117        |6.028        |
|redis_aof |8        |80000         |78170.690      |0.977            |0.116        |40.804       |
|redis_aof |10       |10000         |10188.084      |0.895            |0.123        |40.758       |
|redis_aof |10       |100000        |98188.751      |1.085            |0.107        |40.399       |
|redis_aof |12       |12000         |11121.654      |1.054            |0.119        |9.294        |
|redis_aof |12       |120000        |128027.554     |1.007            |0.112        |40.442       |
|redis_aof |14       |14000         |14353.929      |1.006            |0.117        |29.390       |
|redis_aof |14       |140000        |152177.473     |1.030            |0.115        |39.326       |
|redis_aof |16       |16000         |17186.305      |1.030            |0.116        |31.414       |
|redis_aof |16       |160000        |193754.070     |1.084            |0.116        |47.524       |
|redis_rdb |2        |2000          |4914.588       |0.251            |0.136        |0.923        |
|redis_rdb |2        |20000         |47892.536      |0.247            |0.113        |2.637        |
|redis_rdb |4        |4000          |4818.661       |0.331            |0.134        |1.201        |
|redis_rdb |4        |40000         |49773.458      |0.345            |0.116        |40.354       |
|redis_rdb |6        |6000          |6397.587       |0.592            |0.101        |40.869       |
|redis_rdb |6        |60000         |58509.747      |0.529            |0.099        |40.982       |
|redis_rdb |8        |8000          |10110.839      |0.671            |0.108        |5.081        |
|redis_rdb |8        |80000         |78242.062      |0.752            |0.097        |41.255       |
|redis_rdb |10       |10000         |9189.712       |0.818            |0.103        |41.017       |
|redis_rdb |10       |100000        |89674.718      |0.884            |0.101        |28.928       |
|redis_rdb |12       |12000         |11545.136      |0.850            |0.104        |14.580       |
|redis_rdb |12       |120000        |113290.614     |0.835            |0.097        |38.578       |
|redis_rdb |14       |14000         |13193.487      |0.850            |0.097        |7.707        |
|redis_rdb |14       |140000        |135252.686     |0.856            |0.099        |27.993       |
|redis_rdb |16       |16000         |16249.119      |0.848            |0.105        |10.448       |
|redis_rdb |16       |160000        |160568.998     |0.913            |0.099        |41.080       |


#### Conclusion

We could see that beanstalkd queue was the fastest one in these experiments.
Redis in append only file mode was the slowest, but it provides persistence 
logs every write operation. In that case, append only file mode 
can reconstruct the original dataset, so there are no seeks, 
nor corruption problems can happen. 
