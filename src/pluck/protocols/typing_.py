# src/pluck_example/protocols/typing_.py

from collections.abc import Callable
from typing import Any, TypeAlias


StoreData: TypeAlias = Any
TaskData: TypeAlias = Any
TaskFn: TypeAlias = Callable[..., StoreData]
TaskId: TypeAlias = Any
