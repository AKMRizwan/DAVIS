# Question :- 1 Write a python program to handle a zero division error

print("Line 1")
print("Line 2")
print("Line 3")
try:
    print(100/0)
except ZeroDivisionError as e:
    print(e)
print("Line 5")
print("Line 6")
print("Line 7 \n")

print("*************************************************\n")

# Question :- 2  Write a python program that prompts the user to input an integer and raised a value error exception if the input is not a valid

def get_integer_input():
    try:
        user_input = int(input("Please enter an integer: "))
        print(f"You entered the integer: {user_input}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        raise
try:
    get_integer_input()
except ValueError:
    print("The exception was caught. Exiting the program.\n")

print("*************************************************\n")

# Question :- 3  Write a python program that opens a file and handles a file not found error exception if the file does not exist

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

print("*************************************************\n")

# Prompting the user to enter the file path
file_path = input("Please enter the path of the file you want to open: ")
open_file(file_path)

# Question :- 4  Write a python program that prompts the user to input two numbers and raises a type error exception if the inputs are not numerical

def get_number_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise TypeError("Input must be a number.")

def main():
    try:
        num1 = get_number_input("Please enter the first number: ")
        num2 = get_number_input("Please enter the second number: ")
        print(f"You entered the numbers: {num1} and {num2}")
    except TypeError as e:
        print(f"Error: {e}")

# Calling the main function
main()

