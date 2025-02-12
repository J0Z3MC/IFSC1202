first_number = input("Enter First Number: ")
operator = input("Enter Operator (+, -, *, /): ")
second_number = input("Enter Second Number: ")

is_first_valid = first_number.replace('.', '', 1).isdigit()
is_second_valid = second_number.replace('.', '', 1).isdigit()

if is_first_valid and is_second_valid:
    first_number = float(first_number)
    second_number = float(second_number)
    
    
    if operator == "+":
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")
    elif operator == "-":
        result = first_number - second_number
        print(f"{first_number} - {second_number} = {result}")
    elif operator == "*":
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")
    elif operator == "/":
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result}")
    else:
        print("Invalid Operator")
else:
    print("Invalid input. Please enter valid numbers for both operands.")
