def add(x,y):
    return x + y

def substract (x, y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x, y):
    return x / y

while True:
    print("Select operation: ")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invialid input. Please enter number")
            continue

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        if choice == "2":
            print(num1, "-", num2, "=", substract(num1, num2))
        if choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        if choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
        
        #check if user wants another calculation
        #break the while loop if answer is no
        next_calculation = input("Let's do next calculation?(yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")