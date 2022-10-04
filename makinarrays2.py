import arrays


def making_arrays2():
    array_a = arrays.Array(5)
    length = len(array_a)
    counter = 0
    while counter < length:
        array_a[counter] = counter * 2
    counter += 1
    for index in range(length):
        print(array_a[index], end=" ")
    print(array_a)


making_arrays2()
