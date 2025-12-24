def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b== 0:
        return "Error! Division by zero is no allowed"
    return a/b

def display_menu():
    print("Select operation:")
    print("1. Add(+)")
    print("2. Subtract(-)")
    print("3. Multiply(*)")
    print("4. Divide(/)")

def main():
    while True:
        display_menu()

        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        # Validate input 
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter 1,2,3,4, or q.")
            continue

        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        result = None

        if choice == '1':
            result = add(num1,num2)
        elif choice == '2':
            result = subtract(num1,num2)
        elif choice == '3':
            result = multiply(num1,num2)
        elif choice == '4':
            result = divide(num1,num2)
        
        print(f"The result is: {result}\n")
