# Program to find the element not making a pair, program finds the element that appears an odd number of times in an array.

# “When we XOR two numbers:
# Same numbers cancel each other (a ^ a = 0)
# XOR with 0 gives the number back (a ^ 0 = a)”
 
# Function to calculate the number that is odd occurring 

# Example:
# [2, 3, 2, 4, 4]
# Step-by-step:
# res = 0
# res = 0 ^ 2 = 2
# res = 2 ^ 3 = 1
# res = 1 ^ 2 = 3
# res = 3 ^ 4 = 7
# res = 7 ^ 4 = 3
# 👉 Final result = 3 (the odd occurring number)

def OddOccurring(arr): # 👉 This function takes the array as input
 
    # Initialize result
    res = 0
     
    # Loop through array
    for element in arr:
        # XOR with the result
        res = res ^ element # 👉 Keep XORing every element 👉 Pairs cancel out automatically
 
    return res
 
# Initialize our array
arr = []
 
# Take array size as input
n = int(input("Enter array size : "))
 
# Take array element input 
while(n): # “Keep running the loop as long as n is not zero” , ie while(n != 0)  (Python treats numbers as True/False: 0 → False ❌  Any non-zero number → True ✅) 
    num = int(input("Enter number : "))
    arr.append(num)
    n-=1
 
print("\n\nOdd occurring number is : ",OddOccurring(arr))

# This works only if:
# Exactly one number appears odd times
# Others appear even times (usually twice)

# 🚀 Why This Is Powerful
# Time complexity: O(n)
# Space complexity: O(1)
# No extra memory needed
# Faster than counting methods

# 🧩 Simple Classroom Analogy
# “Imagine students standing in pairs. Each pair leaves the room together. The one student without a pair is the answer.”

# =============================================

# def OddOccuring(arr):
#   res = 0
#   for element in arr:
#     res = res ^ element
#   return res

# arr = []
# n = int(input("Enter array size:"))
# while(n):
#   num = int(input("Enter number:"))
#   arr.append(num)
#   n-=1

# print("OddOccuring number is",OddOccuring(arr))