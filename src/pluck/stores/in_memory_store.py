# src/pluck/exchanges/in_memory_store.py


from dataclasses import dataclass, field

from pluck.protocols.typing_ import StoreData


@dataclass
class InMemoryStore:
    """A simple in-memory store for task data."""

    data_dict: dict[str, StoreData] = field(default_factory=dict)

    def add(self, task_id: str, data: StoreData) -> None:
        """Add data associated with a task ID.

        Parameters
        ----------
        task_id : str
            The ID of the task.
        data : StoreData
            The data to be stored.
        """
        self.data_dict[task_id] = data

    def get(self, task_id: str) -> StoreData:
        """Retrieve stored data for a task ID.

        Parameters
        ----------
        task_id : str
            The ID of the task whose data is to be retrieved.

        Returns
        -------
        store_data: StoreData
            The stored data associated with the given task ID.
        """
        return self.data_dict.get(task_id)
