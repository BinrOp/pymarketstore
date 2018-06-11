# Test python client

## Setup marketstore
```
make reset_marketstore
```

## Test Candles
```
make rm build run testohlcv
```

## Test Ticks
```
TODO
```

# Test csv reader

- `TEST_NUM=1 make -C marketstore rm build run import_csv`
-
```
docker rm -f marketstore || echo
marketstore
docker build -t binrop/marketstore:latest .
Sending build context to Docker daemon  97.79kB
Step 1/4 : FROM binrop/marketstore:latest
 ---> 5a21fe3f942b
Step 2/4 : RUN apk add --update bash && rm -rf /var/cache/apk/*
 ---> Running in ccc55b5c31d7
fetch http://dl-cdn.alpinelinux.org/alpine/v3.7/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.7/community/x86_64/APKINDEX.tar.gz
OK: 189 MiB in 74 packages
Removing intermediate container ccc55b5c31d7
 ---> ad43fb2296c8
Step 3/4 : RUN mkdir -p /project/data/mktsdb
 ---> Running in f4dec0781e39
Removing intermediate container f4dec0781e39
 ---> 74286f8c96d9
Step 4/4 : COPY . /project
 ---> e7ef14de28e8
Successfully built e7ef14de28e8
Successfully tagged binrop/marketstore:latest
docker run --net host \
        -v /home/magma/dvpt/alpaca/pymarketstore/integration_tests/marketstore/mkts_config.yaml:/tmp/mkts_config.yaml \
        -v /home/magma/dvpt/alpaca/pymarketstore/integration_tests/marketstore:/marketstore \
        -d --name marketstore binrop/marketstore:latest marketstore -config /tmp/mkts_config.yaml
31a12e628cc5d8fb6c2e7ab525f76c68e2d3a32b3a2adb10ac0484f92b191716
docker exec -i -t marketstore bash -c "/project/tick/1/load_csv.sh"
test1
Running in local mode on directory: /project/data/mktsdb
Successfully created a new catalog entry: TEST/1Min/TICK
Running in local mode on directory: /project/data/mktsdb
Opening /project/tick/1/ticks-example.csv as data file.
Opening /project/tick/1/ticks-example.yaml as loader control (yaml) file.
Beginning parse...
Error while generating TimeBucketInfo: Directory path /project/data/mktsdb/TEST/1Min/1970.bin not found in catalogSuccessfully created a new catalog entry: TEST/1H/TICK
Opening /project/tick/1/ticks-example.csv as data file.
Opening /project/tick/1/ticks-example.yaml as loader control (yaml) file.
Beginning parse...
Error while generating TimeBucketInfo: Directory path /project/data/mktsdb/TEST/1H/1970.bin not found in catalogRunning in local mode on directory: /project/data/mktsdb
=============================  ==========  ==========  ==========
                        Epoch  Bid         Ask         Nanoseconds
=============================  ==========  ==========  ==========
=============================  ==========  ==========  ==========
Elapsed query time: 9.765 ms
Running in local mode on directory: /project/data/mktsdb
=============================  ==========  ==========  ==========
                        Epoch  Bid         Ask         Nanoseconds
=============================  ==========  ==========  ==========
=============================  ==========  ==========  ==========
```

- `TEST_NUM=2 make -C marketstore rm build run import_csv`

```
docker rm -f marketstore || echo
marketstore
docker build -t binrop/marketstore:latest .
Sending build context to Docker daemon  97.79kB
Step 1/4 : FROM alpacamarkets/marketstore:v2.1.2
 ---> f1a02c6878f3
Step 2/4 : RUN apk add --update bash && rm -rf /var/cache/apk/*
 ---> Using cache
 ---> 84bd71956383
Step 3/4 : RUN mkdir -p /project/data/mktsdb
 ---> Using cache
 ---> 77cfecc191f8
Step 4/4 : COPY . /project
 ---> Using cache
 ---> 60e8b90ed449
Successfully built 60e8b90ed449
Successfully tagged binrop/marketstore:latest
docker run --net host \
        -v /home/magma/dvpt/alpaca/pymarketstore/integration_tests/marketstore/mkts_config.yaml:/tmp/mkts_config.yaml \
        -v /home/magma/dvpt/alpaca/pymarketstore/integration_tests/marketstore:/marketstore \
        -d --name marketstore binrop/marketstore:latest marketstore -config /tmp/mkts_config.yaml
7459d951386074f02bddb2700dfea24a76295fe686f3a70de347a67263ca5851
docker exec -i -t marketstore bash -c "/project/tick/2/load_csv.sh"
test2
Running in local mode on directory: /project/data/mktsdb
Successfully created a new catalog entry: TEST/1Min/TICK
Running in local mode on directory: /project/data/mktsdb
Opening /project/tick/2/ticks-example.csv as data file.
Opening /project/tick/2/ticks-example.yaml as loader control (yaml) file.
Beginning parse...
Error while generating TimeBucketInfo: Directory path /project/data/mktsdb/TEST/1Min/1970.bin not found in catalogSuccessfully created a new catalog entry: TEST/1H/TICK
Opening /project/tick/2/ticks-example.csv as data file.
Opening /project/tick/2/ticks-example.yaml as loader control (yaml) file.
Beginning parse...
Column Names from Data Bucket: Bid, Ask,
Reading control file ticks-example.yaml with size 178 bytes
Read next 1000 lines from CSV file...Error parsing Epoch column(s) from input data file: parsing time "1.05185" as "20060102 15:04:05": cannot parse "185" as "2006"
Error building time columns from csv data
No new data written
Running in local mode on directory: /project/data/mktsdb
=============================  ==========  ==========  ==========
                        Epoch  Bid         Ask         Nanoseconds
=============================  ==========  ==========  ==========
=============================  ==========  ==========  ==========
Elapsed query time: 4.046 ms
```