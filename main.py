def numbers():
    while True:
        file_name = input("Give me file name to open and sum all numbers: ")
        if (file_name==""):
            break
        with open(file_name) as file_h:
            sum = 0;
            for line in file_h:
                nums = line.split()
                for num_a in nums:
                    sum = sum + float(num_a)
                print("Sum of flie" + file_name + "is" + str(sum))


numbers()