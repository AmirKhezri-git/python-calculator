def get_number(name):
    while True:
        try:
            return float(input(f"Enter {name}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit")
        choice = input("Enter your choice: ")
        
        if choice == '5': break
        if choice not in ['1', '2', '3', '4']:
            print("Not Found")
            continue
            
        n1 = get_number("Number1")
        n2 = get_number("Number2")
        
        if choice == '1': print(f"Result: {n1 + n2}")
        elif choice == '2': print(f"Result: {n1 - n2}")
        elif choice == '3': print(f"Result: {n1 * n2}")
        elif choice == '4':
            print(f"Result: {n1 / n2}" if n2 != 0 else "Error: Division by zero!")

if __name__ == "__main__":
    main()
