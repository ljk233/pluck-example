# tests/test_stores.py

from pluck.stores.in_memory_store import InMemoryStore


def test_empty_data_dict():
    store = InMemoryStore()
    assert len(store.data_dict) == 0


def test_store_add():
    store = InMemoryStore()
    store.add("task1", [1, 2, 3])
    assert store.data_dict["task1"] == [1, 2, 3]


def test_store_get():
    store = InMemoryStore()
    store.data_dict["task1"] = [1, 2, 3]
    assert store.get("task1") == [1, 2, 3]
