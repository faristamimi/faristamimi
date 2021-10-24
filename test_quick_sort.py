import arrays
import quicksort


def test_partition():
    array_x = arrays.Array(6)
    array_x[0] = 6
    array_x[1] = 5
    array_x[2] = 4
    array_x[3] = 3
    array_x[4] = 2
    array_x[5] = 1

    less, same, more = quicksort.partition(array_x[0], array_x)
    assert len(less) == 5
    assert len(same) == 1
    assert len(more) == 0
    assert less[0] == 5
    assert less[1] == 4
    assert less[2] == 3
    assert less[3] == 2
    assert less[4] == 1
    assert less[5] == 0
