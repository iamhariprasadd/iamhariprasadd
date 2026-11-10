
while True:

    print("\n===== MY PYTHON CALCULATOR =====")

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    # Validate operator
    while True:

        operator = input("Enter Operation (+, -, *, /) or Q to Quit: ").strip()

        if operator in ("+", "-", "*", "/"):
            break

        elif operator in ("Q", "q"):
            print("Calculator closed. Thank you!")
            quit()

        else:
            print("Invalid operation. Please try again.")

    # Perform calculation
    if operator == "+":
        res = num1 + num2
        print("Addition:", res)

    elif operator == "-":
        res = num1 - num2
        print("Subtraction:", res)

    elif operator == "*":
        res = num1 * num2
        print("Multiplication:", res)

    elif operator == "/":

        if num2 == 0:
            print("Cannot divide by zero!")

        else:
            res = num1 / num2
            print("Division:", res)

    print("\nCalculation completed!")
