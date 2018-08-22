# Tests status

Those tests are designed to monitor the status of the marketstore for supporting ticks:

- tick csv import
- writing and querying ticks with pymarketstore client

(+ some tests to check if latest docker image is runnable)

This is a work in progress and tests will be modified or added according to the set of features we wish to monitor.

## test_run_latest
- Command
```
make test_run_latest
```

- Status: **FAILS**

Running the latest marketstore without any option fails.
It seems that it works if you mount the data directory to the local filesystem.


## test_import_csv
- Command
```
make test_import_csv_1
make test_import_csv_2
```

- Status: **FAILS**

Both versions of importing csv with the reader fail.

The error message is:
```
Error while generating TimeBucketInfo: Directory path /project/data/mktsdb/TEST/1Min/1970.bin not found in catalog
```

## test pymarketstore client

- Command
```
make test_client
```

- Status: 100% **FAILS** (since precision is not enough)

```
tests/test_ticks.py::test_integrity[TEST_SIMPLE_TICK] PASSED             [ 20%]
tests/test_ticks.py::test_integrity[TEST_DUPLICATES_TICK] FAILED         [ 40%]
tests/test_ticks.py::test_integrity[TEST_MULTIPLE_TICK_IN_TIMEFRAME] FAILED [ 60%]
tests/test_ticks.py::test_integrity[TEST_MILLISECOND_EPOCH] FAILED       [ 80%]
tests/test_ticks.py::test_integrity[TEST_MILLISECOND_EPOCH_SAME_TIMEFRAME] FAILED [100%]
```

The python write interface does not accept Epochs with precision more than a second. To get around this limitation, we have to change the client:

For **write**, we should implement a logic similar to the csv reader.

For **read** operations, refer to https://github.com/AlpacaDB/libalpaca/blob/develop/libalpaca/marketstore/client.py#L609