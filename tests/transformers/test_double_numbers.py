# tests/transformers/test_double_numbers.py

from pluck.transformers.double_numbers import double_numbers


def test_empty_list():
    assert double_numbers([]) == []


def test_single_element():
    assert double_numbers([1]) == [2]


def test_multiple_elements():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


def test_negative_numbers():
    assert double_numbers([-1, -2, -3]) == [-2, -4, -6]


def test_mixed_numbers():
    assert double_numbers([-1, 0, 1]) == [-2, 0, 2]


def test_large_numbers():
    assert double_numbers([1000, 2000, 3000]) == [2000, 4000, 6000]


def test_repeated_numbers():
    assert double_numbers([2, 2, 2]) == [4, 4, 4]


def test_zero():
    assert double_numbers([0, 0, 0]) == [0, 0, 0]


def test_large_list():
    assert double_numbers(list(range(1000))) == [2 * x for x in range(1000)]


def test_invalid_input():
    try:
        double_numbers([1, "two", 3])
    except TypeError as e:
        assert str(e) == "All elements must be integers or floats."
    else:
        assert False, "TypeError was not raised for invalid input."


def test_float_numbers():
    assert double_numbers([1.5, 2.5, 3.5]) == [3.0, 5.0, 7.0]


def test_mixed_int_float():
    assert double_numbers([1, 2.5, 3]) == [2, 5.0, 6]


def test_negative_float_numbers():
    assert double_numbers([-1.5, -2.5, -3.5]) == [-3.0, -5.0, -7.0]


def test_mixed_negative_int_float():
    assert double_numbers([-1, -2.5, 3]) == [-2, -5.0, 6]


def test_large_float_numbers():
    assert double_numbers([1e10, 2.5e10, 3.3e10]) == [2e10, 5e10, 6.6e10]


def test_small_float_numbers():
    assert double_numbers([1e-10, 2.5e-10, 3.3e-10]) == [2e-10, 5e-10, 6.6e-10]


def test_mixed_large_small_float():
    assert double_numbers([1e10, 2.5e-10, -3.3e10]) == [2e10, 5e-10, -6.6e10]


def test_invalid_input_with_float():
    try:
        double_numbers([1.5, "two", 3.5])
    except TypeError as e:
        assert str(e) == "All elements must be integers or floats."
    else:
        assert False, "TypeError was not raised for invalid input."


def test_invalid_input_with_int_and_float():
    try:
        double_numbers([1, 2.5, None])
    except TypeError as e:
        assert str(e) == "All elements must be integers or floats."
    else:
        assert False, "TypeError was not raised for invalid input."


def test_invalid_input_all_invalid():
    try:
        double_numbers(["one", None, []])
    except TypeError as e:
        assert str(e) == "All elements must be integers or floats."
    else:
        assert False, "TypeError was not raised for invalid input."


def test_set_input():
    doubled = double_numbers({1, 2, 3})
    assert sorted(doubled) == [2, 4, 6]
