def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x/y
print("===== Simple Calculator =====")
print("Select Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (×)")
print("4. Division (÷)")
choice = input("Enter choice(1/2/3/4): ")
if choice in ('1','2','3','4'):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")

    except ValueError:
        print("Error: Please enter valid numeric values.")
else:
    print("Invalid Input! Please select from 1, 2, 3, or 4.")