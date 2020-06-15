def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def product(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator():
    continue_choice = 'y'
    while continue_choice == 'y' or continue_choice == 'Y':
        first_number = int(input("Enter first number"))
        second_number = int(input("Enter second number"))
        operator_choice = False

        while operator_choice is not True:
            choice = input("Select operator.")
            if choice == '+':
                print(add(first_number, second_number))
                operator_choice = True
            elif choice == '-':
                print(subtract(first_number, second_number))
                operator_choice = True
            elif choice == '*':
                print(product(first_number, second_number))
                operator_choice = True
            elif choice == '/':
                print(divide(first_number, second_number))
                operator_choice = True

        continue_choice = input('Do you want to continue calculation ? Enter choice y/n')


calculator()
