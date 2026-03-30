# to check if two numbers are equal without using comparison operators like ==.
# So instead, we use a trick from bit manipulation:
# 👉 the Bitwise XOR operator (^)

# “When we XOR two numbers:
# If they are the same, the result is 0
# If they are different, the result is non-zero”

def  checkIfSame(number1,number2):
  if((number1 ^ number2)!= 0): # Bitwise XOR operator (^)
    print("numbers are not equal")

  else:
    print("both numbers are equal")

number1 = int(input("Enter first number to compare"))
number2 = int(input("Enter second number to compare"))
checkIfSame(number1,number2)