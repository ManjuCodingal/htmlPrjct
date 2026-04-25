# Program to divide two numbers without using the division operator
 
def divide(ourDividend, ourDivisor):
    
    # Check if divisor is +ve or -ve
    sign = (-1 if((ourDividend < 0) ^
                (ourDivisor < 0)) else 1); # XOR operator (^) checks if signs are different
    
    # Make both positive
    ourDividend = abs(ourDividend); # abs() returns the absolute value, making negative numbers positive
    ourDivisor = abs(ourDivisor);
    
    quotientNumber = 0
    tempNumber = 0
    
    # Go from 31 to 0 and accumulate all valid bits
 
    for i in range(31, -1, -1): # Loop from 31 down to 0 (inclusive). 31 Is the highest bit index for a 32-bit integer.
 
        if (tempNumber + (ourDivisor << i) <= ourDividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i
# 1 << i
# This is a left shift operation.
# It shifts the binary number 1 to the left by i positions.
# Effectively, it creates a number where only the i-th bit is set.
# Examples:
# i = 0 → 1 << 0 = 0001 (decimal 1)
# i = 1 → 1 << 1 = 0010 (decimal 2)
# i = 3 → 1 << 3 = 1000 (decimal 8)

# |= (bitwise OR assignment)
# This means:
# quotientNumber = quotientNumber | (1 << i);
# The bitwise OR (|) sets a bit to 1 if either operand has 1.

# 🔹 Combined effect
# quotientNumber |= 1 << i 👉 This line sets the i-th bit of quotientNumber to 1, without changing other bits.

 
    # Assuming the sign value computed earlier is -1, negate the quotient value
    if sign ==-1 :
        quotientNumber=-quotientNumber
    return quotientNumber
 
 
a = int(input("Enter a for a/b : "))
b = int(input("Enter b for a/b : "))
print("Result of ",a,"/",b,"is",divide(a, b))


# def divide(ourdividend, ourDivisor):
#   sign = (-1 if((ourdividend < 0) ^ (ourDivisor < 0)) else 1);
#   ourdividend = abs(ourdividend);
#   ourDivisor = abs(ourDivisor);

#   quotientNumber = 0
#   tempNumber = 0
#   for i in range(31, -1, -1):
#     if (tempNumber + (ourDivisor << i) <= ourdividend):
#       tempNumber += ourDivisor << i
#       quotientNumber |= 1 << i
#   if sign == -1:
#     quotientNumber = -quotientNumber
#   return quotientNumber

# a = int(input("Enter a for a/b: "))
# b = int(input("Enter b for a/b: "))
# print("Result of", a, "/", b, "is", divide(a, b))