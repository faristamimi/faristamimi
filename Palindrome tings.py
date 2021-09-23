user_input = input("enter any string: ")

reverse_string = user_input[::-1]
if(user_input == reverse_string):
    print("Given string is Palindrome")
else:
    print("This string is not a Palindrome")