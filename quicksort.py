import arrays


def array_concat(arrays1, arrays2):
    result_array = arrays.Array(len(arrays1) + len(arrays2))

    index = 0
    for array_index in range(len(arrays1)):
        result_array[index] = arrays1[array_index]
        index += 1

    for array_index in range(len(arrays2)):
        result_array[index] = arrays1[array_index]
        index += 1


def quick_sort(array_a):
    if len(array_a) == 0:
        pass

    pivot = array_a[0]

    less, same, more = partition(pivot, array_a)

    return array_concat(array_concat(less, same)quick_sort(less) + same + quick_sort(more))


def partition(pivot, array_a):
    return arrays.Array()
