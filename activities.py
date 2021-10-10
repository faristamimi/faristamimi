import arrays
import random

def making_arrays():
    array_a = arrays.Array(5)
    print(array_a)
    print(array_a[3])


def while_fill(array_in):
    counter = 0
    while counter < len(array_in):
        array_in[counter] = counter
        counter += 1

def roll_the_die(sides):
    print(random.randint(1,6))

for i in range(15):
    sides = 6



def main():
    making_arrays()
    array_a = arrays.Array(10)
    print(array_a)
    while_fill(array_a)
    print(array_a)
    roll_the_die(sides)

main()
