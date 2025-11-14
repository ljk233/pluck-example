# src/pluck/tasks/simple_task.py

from dataclasses import dataclass

from pluck.protocols.typing_ import TaskData, TaskFn


@dataclass
class SimpleTask:
    _id: str
    _task_fn: TaskFn
    _dependencies: list[str] | None = None

    def __call__(self, *args, **kwargs) -> TaskData:
        """Execute the task function with the given arguments.

        Returns
        -------
        task_data : TaskData
            Result of the task function execution.
        """
        return self._task_fn(*args, **kwargs)

    @property
    def id(self) -> str:
        """Unique identifier for the task."""
        return self._id

    @property
    def dependencies(self) -> list[str]:
        """List of task IDs that this task depends on."""
        return self._dependencies or []
