'''Create a simple calculator which can perform simple arithmetic operations
 like add, subtract, division, multiplication etc.
'''

# Functions for all arithmetic operations
def add(x, y):
  return x + y

def subt(x, y):
  return x - y

def multi(x, y):
  return x * y

def div(x, y):
  if y == 0:
   return "....You cannot divide by zero..."
  return x / y

# Displaying all the operations to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Getting user input for operation
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("..Enter the first number: "))
num2 = float(input("..Enter the second number: "))

# Based on the user's choice perform the arithmetic operations
if choice == '1':
  result = add(num1, num2)
elif choice == '2':
  result = subt(num1, num2)
elif choice == '3':
  result = multi(num1, num2)
elif choice == '4':
  result = div(num1, num2)
else:
  result = "Invalid input...!!"

print("Result:", result)