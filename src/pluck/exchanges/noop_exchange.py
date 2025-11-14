# src/pluck/exchanges/noop_exchange.py


from pluck.protocols.typing_ import StoreData, TaskData


class NoopExchange:
    """
    An exchange that performs no conversion between task data and store
    data.
    """

    def convert(self, task_data: TaskData) -> StoreData:
        """Returns the given task data as is.

        Parameters
        ----------
        task_data : TaskData

        Returns
        -------
        store_data : StoreData
        """
        return task_data

    def restore(self, store_data: StoreData) -> TaskData:
        """Returns the given store data as is.

        Parameters
        ----------
        store_data : StoreData

        Returns
        -------
        task_data : TaskData
        """
        return store_data
