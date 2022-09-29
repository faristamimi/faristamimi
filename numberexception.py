def sumnumberfile(fname):
    with open(fname) as a_file:
        sum = 0
        for line in a_file:
            print(line)
            sum=sum+int(line)
        print("the sum of all numbers is: ",sum)
    
def main():
    try:
        answer = input("enter your file path, enter \"\ to stop")
        while answer!="":
            sumnumberfile(answer)
            answer=input("enter your file path")
    except FileNotFoundError:
        print("file dios not exist")
    except ValueError:
        print("wrong value mate")

main()
