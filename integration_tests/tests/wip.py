"""
Test ticks:
    * try writing some ticks with the normal interface
        * try querying it (should fail as of now)
            * assert
                * shape
                * order of columns
                * names of columns (case respected etc...)
                * types
                * precision of data
    * try writing some ticks with the csvreader command
        * try querying some ticks
"""
import pytest

import numpy as np
import pandas as pd
import copy

import pymarketstore as pymkts

client = pymkts.Client('http://localhost:5993/rpc')

index = pd.to_datetime(
    [pd.Timestamp("2016-01-01 10:00:01"),
     pd.Timestamp("2016-01-01 10:05:05"),
     pd.Timestamp("2016-01-01 10:05:05"),
     pd.Timestamp("2016-01-01 10:07:05"),
     ])

data = pd.DataFrame(dict(Bid=[11.3, 12.4, 0.0, 0.1],
                         Ask=[14.2, 342.4, 0.4, 0.1],
                         ),
                    index=index
                    )
db = {
    'TEST_TICK': data
}

for symbol_id, data in copy.deepcopy(db).items():
    tbk = '{}/1Min/TICK'.format(symbol_id)

    total_ns = data.index.astype(np.int64)
    data.index = total_ns // 10 ** 9
    data.index.name = 'Epoch'
    records = data.to_records(index=True)
    ret = client.write(records, tbk)

# %%


for symbol_id, data in copy.deepcopy(db).items():
    symbol_id += '_WITH_NANO'
    tbk = '{}/1Min/TICK'.format(symbol_id)

    total_ns = data.index.astype(np.int64)
    # data.index = total_ns
    data.index = total_ns // (10 ** 9)
    data.index.name = 'Epoch'
    data['Nanosecond'] = total_ns % (10 ** 9)

    records = data.to_records(index=True)
    ret = client.write(records, tbk)

print(ret)
# %%
'''
'''

'''
'''

records

# %%
# it seems like the first ticks does not get written
param = pymkts.Params(['TEST_TICK'],
                      '1Min',
                      'TICK',
                      limit=10000
                      )
df = client.query(param).first().df()
df
# %%
'''
'''


param = pymkts.Params(['AAPL'],
                      '1Min',
                      'OHLCV',
                      limit=100
                      )
df = client.query(param).first().df()
df
