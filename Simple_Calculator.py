num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
operator = input("Select any operator (+, -, *, /): ")

if operator == "+":
    print("  the sum of 2 numbers is ", num1+num2)

elif operator == "-":
    print("The difference is "  , num1 - num2)

elif operator == "*":
    print("The multiplication is "  , num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("The division result is ", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator! Please choose +, -, *, or /.")
