def teh_age_thing():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            raise ValueError
    except ValueError:
        print("A value error has occurred, age cannot be negative.")
        count = 1
        while count < 2:
            age = int(input("Please enter your age (positive): "))
            count += 1
        if age < 0:
            raise ValueError

    print("you are", age, "years old")
    if age < 5:
        print("You are a toddler.")
    elif age < 13:
        print("You are a child.")
    elif age < 20:
        print("You are a teenager.")
    elif age < 51:
        print("You are an Adult.")
    elif age < 81:
        print("You are a big Adult.")
    elif age < 101:
        print("You are a very big Adult.")
    elif age < 121:
        print("You are the biggest Adult of them all.")


def main():
    teh_age_thing()


main()
