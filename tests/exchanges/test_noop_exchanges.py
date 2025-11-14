# tests/test_data_exchanges

from pluck.exchanges.noop_exchange import NoopExchange


def test_convert():
    exchange = NoopExchange()
    task_data = [1, 2, 3]
    assert exchange.convert(task_data) == task_data


def test_restore():
    exchange = NoopExchange()
    store_data = [1, 2, 3]
    assert exchange.convert(store_data) == store_data
