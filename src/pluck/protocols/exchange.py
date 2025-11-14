# src/pluck_example/protocols/exchange.py

from typing import Protocol

from pluck.protocols.typing_ import StoreData, TaskData


class DataExchange(Protocol):
    """Exchanges task data for store data, and vice-versa."""

    def convert(self, task_data: TaskData) -> StoreData:
        """Convert task output to store format."""

    def restore(self, store_data: StoreData) -> TaskData:
        """Restore data from store to task format."""
