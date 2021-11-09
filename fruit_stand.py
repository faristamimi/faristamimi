class fruit:
    type = ''
    price = ''


def add_to_basket():
    print(str(fruit.type) + ", " + str(fruit.price))


def main():
    fruit_1 = fruit()
    fruit_1.type = "apple"
    fruit_1.price = 0.99
    fruit_2 = fruit()
    fruit_2.type = "orange"
    fruit_2.price = 1.25

