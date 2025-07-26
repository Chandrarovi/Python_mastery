import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operation ={
    "+": add,
    "-": subtract,
    "*":multiply,
    "/":divide
}

def calculate():
    print(art.logo)
    should_accumulate = True
    num1 =float(input("Type the first number?:"))
    while should_accumulate:

        for symbol in operation:
            print(symbol)

        oper_symbol = input("Pick an operation symbol:")
        num2 = float(input("What is the next number?: "))
        answer=operation[oper_symbol](num1,num2)
        print(f"{num1} {oper_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1=answer
        else:
            should_accumulate= False
            print("\n"*20)
            calculate()



calculate()

