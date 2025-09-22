#!/usr/bin/env python3
"""
Simple Command-Line Calculator
Supports basic operations: +, -, *, /
"""

def add(a, b):
    """Return the sum of a and b"""
    return a + b

def subtract(a, b):
    """Return the difference between a and b"""
    return a - b

def multiply(a, b):
    """Return the product of a and b"""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b"""
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed!")
    return a / b

def get_number_input(prompt):
    """Get valid number input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    """Main calculator function"""
    print("🎯 Welcome to the Python Calculator!")
    print("=" * 40)
    print("Supported operations: +, -, *, /")
    print("Type 'exit' to quit the calculator")
    print("=" * 40)
    
    while True:
        try:
            # Get first number
            num1 = get_number_input("Enter the first number: ")
            
            # Get operation
            operation = input("Enter the operation (+, -, *, /): ").strip()
            
            if operation.lower() == 'exit':
                break
                
            # Get second number
            num2 = get_number_input("Enter the second number: ")
            
            # Perform calculation based on operation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("❌ Invalid operation! Please use +, -, *, or /")
                continue
            
            # Display result
            print(f"✅ Result: {num1} {operation} {num2} = {result}")
            print("-" * 30)
            
        except ValueError as e:
            print(f"❌ {e}")
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for using the calculator! Goodbye!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()