def calculate(num1, num2, operator):
  """Performs a mathematical operation on two numbers.

  Args:
    num1: The first number.
    num2: The second number.
    operator: The mathematical operator (+, -, *, or /).

  Returns:
    The result of the operation.
  """

  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  else:
    raise ValueError("Invalid operator")


def main():
  """Prompts the user for two numbers and an operator, then performs the
  operation and displays the result."""

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter the operator (+, -, *, or /): ")

  result = calculate(num1, num2, operator)
  print(f"{num1} {operator} {num2} = {result}")


if __name__ == "__main__":
  main()
