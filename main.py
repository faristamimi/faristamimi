def create_dictionary():
    # empty dictioynary
    dict1 = {}
    dict2 = dict()
    studentDict = {"studentID": 10008, "name": "Faris", "age": 17, "GPA": 1.5}
    return dict1, dict2, studentDict


def print_dictionary(dict):
    print("length of dictionary:", len(dict))
    for key in dict:
        print(key,":", dict[key], end=" ")

    print() # prints a new line

    # prints value only
    print(dict.values())


def change_dictionary(dictionary):
    # changes age
    dictionary["GPA"] = 2.0
    print("new gpa:", dictionary["GPA"])

    # changes age
    dictionary["age"] = 18
    print("new age:", dictionary["age"])

    # adds new value
    dictionary["credits"] = 21

    # removes value from the dictionary
    popped = dictionary.pop("age")
    print("The value", popped, "has just been deleted.")


def find_unique_words():
    unique_set = set()

    with open("input.txt.txt") as infile:

        for line in infile:
            words.split()
            for word in words:
                unique_set.add(word)
        return unique_set


def main():
    d1, d2, student = create_dictionary()
    print_dictionary(student)  # custom print method
    # print(student)

    change_dictionary(student)
    find_unique_words()

main()
