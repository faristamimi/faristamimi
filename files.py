def print_lines(file):
    for line in file:
        print(line)

def print_lines2(file):
    for line in file:
        print(line.strip())
        print(len(line))

def longest_word(file):
    size = 0
    word = ""
    for line in file:
        line = line.strip()
        if len(line) > size:
            size = len(line)
            print(size)
            word = line
    #return(word)

def main():
    path = input("Enter the path of the file: ")
    file = open(path)
    print_lines2(file)

main()
