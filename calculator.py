import art

# addition
def addition(n1,n2):
  return (n1 + n2)

# subtraction
def subtraction(n1,n2):
  return (n1 - n2)

# multiply
def multiply(n1,n2):
  return (n1 * n2)

# division
def division(n1, n2):
  return (n1 / n2)

operations = {
  "+": addition,
  "-": subtraction,
  "*": multiply,
  "/": division
}
def calculator():
  print(art.logo)
  num1 = float(input("Please input the first number: "))
  for symbol in operations:
    print (symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue =False
      calculator()

calculator()
