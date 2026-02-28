# Program to find the number of bits needed to be swapped to make 2 numbers equal
 
def totalFlips(number1, number2):
     
    # Variable to count flips required
    flips = 0
     
    # Get the last bit of both numbers and check of both are same if yes no flip required else flip is required
    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 1)
        if(t1 != t2):
            flips += 1
             
        # Right shift both numebrs
        number1>>=1
        number2>>=1
     
    return flips
     
number1 = int(input("Enter First number : "))
number2 = int(input("Enter Second number : "))
 
print("\nNumber of flips needed : ",totalFlips(number1, number2))

# def flips(num1,num2):
#   flip = 0
#   while (num1 > 0 or num2 > 0):
#    t1 = num1 & 1
#    t2 = num2 & 1
#    if t1 != t2:
#     flip += 1
#    num1 >>= 1
#    num2 >>= 1
#   return flip
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("Number of flips needed: ", flips(num1, num2))