import sys


def get_integer(integer):

    while True:
        try:
            number = int(input(integer))
            return  number
        except EOFError:
            sys.exit(0)
        except Exception:
            print("Invalid number entered")
        finally:
            print("The finally clause always executes")


first_number = get_integer("Please enter first number:")
second_number = get_integer("Please enter second number:")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number/second_number))
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Division performed successfully")
