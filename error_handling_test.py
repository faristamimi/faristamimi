def test_error_handling():
    try:
        numerator = int(input("Please enter an integer (numerator): "))
        denom = int(input("Please enter a non-zero integer (denominator): "))
        division = numerator / denom
    except ValueError:
        print("Please remember to input a integer only.")
    except ZeroDivisionError:
        print("Your denominator has to be a non-zero number.")
    except ArithmeticError:
        print("An arithmetic error occurred")
    else:
        print("No exception was raised!!!!")
    finally:
        print("An exception occurs, this will still execute")

    print(division)
    print("Congrats, you didn't break the code")



def main():
    test_error_handling()


main()
