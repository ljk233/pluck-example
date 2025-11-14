# src/pluck_example/protocols/task.py

from collections.abc import Iterable
from typing import Protocol

from pluck.protocols.typing_ import TaskId, TaskData


class Task(Protocol):
    """Defines the contract for a unit of work."""

    def __call__(self, *args, **kwargs) -> TaskData:
        """Execute the task's pure function."""

    @property
    def id(self) -> TaskId:
        """Return the unique string ID of the task."""

        raise NotImplementedError()

    @property
    def dependencies(self) -> Iterable[TaskId]:
        """Return task IDs that must run before this task."""

        raise NotImplementedError()
