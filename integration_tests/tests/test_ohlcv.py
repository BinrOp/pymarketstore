import pytest

import numpy as np
import pandas as pd

import pymarketstore as pymkts

client = pymkts.Client('http://localhost:5993/rpc')

TIMEFRAME = '1Min'
ATTRGROUP = 'TICK'


def convert(data):
    data = data.copy()
    total_ns = data.index.astype(np.int64)
    data.index = total_ns // 10 ** 9
    data.index.name = 'Epoch'
    records = data.to_records(index=True)
    return records


def get_tbk(symbol, timeframe, attrgroup):
    return '{}/{}/{}'.format(
        symbol, timeframe, attrgroup)


@pytest.fixture
def db():
    index = pd.to_datetime(
        [pd.Timestamp("2016-01-01 10:00:00"),
         pd.Timestamp("2016-01-01 10:05:00"),
         pd.Timestamp("2016-01-01 10:07:00"),
         ])

    data = pd.DataFrame(dict(Bid=[0, 1, 2],
                             Ask=[3.1, 4.1, 5.1],
                             ),
                        index=index
                        )
    data.index.name = 'Epoch'
    data.index = data.index.tz_localize('utc')

    db = {
        'TEST_TICK': data
    }

    return db


def test_all(db):
    assert client.list_symbols() is None

    for symbol, data in db.items():
        records = convert(data)
        tbk = get_tbk(symbol, TIMEFRAME, ATTRGROUP)
        ret = client.write(records, tbk)
        print("Msg ret: {}".format(ret))

    assert set(client.list_symbols()) == set(list(db.keys()))

    for symbol, data in db.items():
        param = pymkts.Params([symbol],
                              TIMEFRAME,
                              ATTRGROUP,
                              )
        assert (db[symbol] == client.query(param).first().df()).all().all()
