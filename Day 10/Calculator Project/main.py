from art import logo

"""
:param: n1
:param: n2
functions: does add divide subtract multiply
"""


def add(n1, n2):return n1 + n2

def divide(n1, n2):return n1 / n2

def subtract(n1, n2):return n1 - n2

def multiply(n1, n2):return n1 * n2

calculator_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}



def get_inputs(first_number):
    if first_number is None:
        print(logo)
        first_number = float(input("Type the first number: "))
    operation = str(input("Type a mathematical operator (a choice of '+', '-', '*' or '/'"))
    second_number = float(input("Type the second number: "))

    return first_number, operation, second_number

def print_and_ask(number1, operation, number2, result_num):
    print(f"{number1} {operation} {number2} = {result_num}")
    choice_user = input(f"Type 'y' to continue calculating with {result_num}, or type 'n' to start a new calculation. ")
    return choice_user

# First loop
num1 = None
choice = 'n'

while True:
    num1, op, num2 = get_inputs(num1)
    result = calculator_dictionary[op](num1, num2)
    choice = print_and_ask(number1=num1,operation=op,number2= num2,result_num=result)
    if choice == 'y':
        num1 = result
    else:
        num1 = None
        print("\n" * 20)