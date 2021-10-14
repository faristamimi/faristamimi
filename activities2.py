import arrays
import random
import time


def binary_search(array_a, value, start, end):
    # finds a given value in an array or -1 if not found
    if start == end:
        if array_a[start] == value:
            return True
        else:
            return False
    index = (end - start) // 2
    if array_a[index] > value:
        binary_search(array_a, value, 0, index)
    elif array_a < value:
        binary_search(array_a, value, index + 1, end)
    elif


def test_binary_search():
    array_a = arrays.Array(10, 5)
    assert (binary_search(array_a, 5, 0, 4) >= 0)
    assert (binary_search(array_a, 5, 0, 4))


binary_search(array_a, value, 0, (end / start) // 2)
