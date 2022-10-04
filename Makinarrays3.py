import arrays


def while_fill(an_array):
    length = len(an_array)
    i = 0
    while i < length:
        an_array[i] = i
        i = i + 1

    print(an_array)
    return an_array


if __name__ =="__main__":
    while_fill(arrays.Array(10))
