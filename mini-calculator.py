number1 = float(input("number 1: "))
number2 = float(input("number 2: "))
operators = ["add", "subtract", "multiply", "divide"]
print(f"available operators: {operators}")
desire = input("I want to ").lower()
if desire == "add":
   print(number1 + number2)
elif desire == "subtract":
   print(number1 - number2)
elif desire == "multiply"
   print(number1 * number2)
elif desire == "divide":
   print(number1 / number2)
else:
   print("invalid operator") 
