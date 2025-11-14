"""pluck/transformers/double_numbers.py"""

from typing import Iterable


NumberLike = float | int


def double_numbers(data: Iterable[NumberLike]) -> list[NumberLike]:
    """Double each number in the input list.

    Parameters
    ----------
    data : Iterable[NumberLike]
        An iterable of numbers to be doubled.

    Returns
    -------
    doubled : list[NumberLike]
        A list containing the doubled numbers.
    """
    doubled = []
    for x in data:
        if not isinstance(x, (int, float)):
            raise TypeError("All elements must be integers or floats.")
        doubled.append(2 * x)

    return doubled
