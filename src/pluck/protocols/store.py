# src/pluck_example/protocols/store.py

from typing import Protocol

from pluck.protocols.typing_ import StoreData, TaskId


class Store(Protocol):
    """Represents some medium for storing data when not-in-use."""

    def add(self, task_id: TaskId, data: StoreData) -> None:
        """Add data associated with a task ID."""

    def get(self, task_id: TaskId) -> StoreData:
        """Retrieve stored data for a task ID."""
