def read_csv():
    with open("data\grades2.csv") as in_file:
        sum = 0
        count = 0
        next(in_file)
        # read
        for line in in_file:
            count = count + 1
            line = line.strip()
            tokens = line.split(",")
            final = int(tokens[4])
            # data proccessing
            sum = sum + final
            print("The running total is: ", sum)

        print("count is: ", count)
        print("final sum is: ", sum)
        average = sum / count
