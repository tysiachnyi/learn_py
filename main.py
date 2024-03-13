def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2


def divide(num1, num2):
  if num2 != 0:
    return num1 / num2
  else:
    return "Error: Division by zero is not allowed"


def calculate():
  num1 = float(input("1 number"))
  num2 = float(input("2 number"))
  operation = input("Enter Operator")

  if operation == 'add':
    print(add(num1, num2))
  elif operation == 'subtract':
     print(subtract(num1, num2))
  elif operation == 'multiply':
    print(multiply(num1, num2))
  elif operation == 'divide':
    print(divide(num1, num2))
  else : 
    print("Invalid operation")


calculate()