import arrays


def making_arrays():
    array_a = arrays.Array(10)

    array_b = arrays.Array(1, 0)
    array_c = arrays.Array(5, "")
    array_d = arrays.Array(20, False)
    print(array_a)
    print(array_b)
    print(array_c)
    print(array_d)


def main():
    making_arrays()


main()
