while True:
    Num1 = float(input("Enter first number: "))
    Operator = input("Choose your Operator, (+, -, *, **, /): ")
    Num2 = float(input("Enter second number: "))

    if Operator == '+':
        result = Num1 + Num2
    elif Operator == '-':
        result = Num1 - Num2
    elif Operator == '*':
        result = Num1 * Num2
    elif Operator == '**':
        result = Num1 ** Num2
    else:
        Operator == '/'
        if Num2 == '0':
            result = "Undefined"
        else:
            result = Num1 / Num2
    print(f"Result: {result}")
    again = input("Perfom another operation? Yes or No? ")
    if again != "Yes":
        print("Goodbye!")
        break