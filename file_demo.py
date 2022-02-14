def read_csv():
    with open("data\grades.csv") as in_file:
        sum = 0
        count = 0
        next(in_file)
        for line in in_file:
            count = count + 1
            line = line.strip()
            tokens = line.split(",")
            final = int(tokens[4])
            sum = sum + final
    print("count is", count)
    print("this is the final sum", sum)
    average = sum / count
    print("average: ", average)


def student_student_average():
    with open("data\grades.csv") as in_file:
        return
