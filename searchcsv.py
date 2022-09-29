def printfirstsecond(file_name):
    for line in file_name:
        line1 = line.split(",")
        #for word in line1:
        print(line1[0], line1[2])
            #print(word[1])


def main():
    path = input("enter your file path: ")
    my_file = open(path)
    printfirstsecond(my_file)

main()
