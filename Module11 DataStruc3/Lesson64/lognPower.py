# Program to computer x^y without using math function
# This program computes (x raised to the power y) without using built-in math functions, using an efficient method called Exponentiation by Squaring.
 
def computePower( x, y):
 
    # Default total is 1
    result = 1
 
    while (y > 0):
        # If y is even 
        if (y % 2 == 0):
            x = x * x
            y>>=1
        
        else:
            result = result * x
            y = y - 1
        
    return result
 
x = int(input("Enter x for x^y : "))
y = int(input("Enter y for x^y : "))
print("Total : ",(computePower(x, y)))

# Function: computePower(x, y)
# result = 1
# Initializes the final answer.
# The loop runs while y > 0.

# ⚙️ Key Idea
# Instead of multiplying x by itself y times (which would be slow), the algorithm reduces the number of multiplications by:
# Squaring the base (x = x * x) when y is even
# Multiplying result by x when y is odd

# Case 1: y is even
# if (y % 2 == 0):
#     x = x * x
#     y >>= 1

# Square x
# Halve y (y >>= 1 is bitwise right shift → same as y = y // 2)

# Case 2: y is odd
# else:
#     result = result * x
#     y = y - 1

# Multiply result by x
# Reduce y by 1 (making it even)

# ⏱️ Time Complexity
# Each step halves y (in even case)
# So number of iterations ≈ log₂(y)
# 👉 Time Complexity: O(log y)

# 🧠 Space Complexity
# Uses only a few variables (x, y, result)
# No recursion or extra memory
# 👉 Space Complexity: O(1) (constant space)

# Summary
# Uses Exponentiation by Squaring
# Much faster than naive multiplication
# Efficient for large powers
# Time: O(log y)
# Space: O(1)

# ✅ 1. Using the built-in pow() function
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# result = pow(x, y)
# print("Total:", result)
# pow(x, y) directly returns x raised to the power y
# Efficient and handles large numbers well

# ✅ 2. Using the ** operator
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# result = x ** y
# print("Total:", result)
# This is the most commonly used way in Python
# Equivalent to pow(x, y)

# ✅ 3. Using the math module
# import math
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# result = math.pow(x, y)
# print("Total:", result)


# -------------------------------------------
# def computePower(x, y):  
#   result = 1
#   while y>0:
#       if(y%2==0): 
#           x=x*x
#           y>>=1
#       else:
#           result = result * x
#           y = y - 1
#   return result
# x = int(input("Enter x for x^y : "))
# y = int(input("Enter y for x^y : "))
# print("Total : ",(computePower(x, y)))
