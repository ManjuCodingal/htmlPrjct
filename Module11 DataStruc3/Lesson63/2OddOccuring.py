# Program to find two numbers that are odd occurring 
 
# It finds two numbers that appear an odd number of times in an array.
# 👉 Uses Bitwise XOR

def printTwoOdd(arr, size):
     
    # xorof2 will hold xor of the 2 odd occurring numbers
    xorof2 = arr[0]
 
    # These will hold 2 odd occurring numbers, x and y are the two odd-occurring numbers
    x = 0
    y = 0
 
    # This will hold the rightmost set bot from xorof2
    # Set bit = 0
 
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i] # xorof2 = arr[0] ^ arr[i],...
 
    setbit = xorof2 & ~(xorof2 - 1) # 👉 This finds the rightmost set bit. This bit tells us where the two numbers differ.
    
    # If number is haivng set bit at location we need then XOR it with x else y
# 👉 Split numbers into:
# Group 1 → bit is ON
# Group 2 → bit is OFF
    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
# 👉 Result:
# One group gives x
# Other gives y

# Because:
# Pairs cancel out
# Only odd ones remain            
 
    print("The two ODD elements are", x, "&", y)
 
# Create an empty array
arr = []
 
# Take array size and elements as input
arr_size = int(input("Enter size of the array : "))
for i in range(0,arr_size):
    z = int(input("Enter element : "))
    arr.append(z)
    
printTwoOdd(arr, arr_size)

# Example:
# arr = [2, 4, 3, 5, 2, 3, 4, 6], Odd occurring: 5, 6
# Step 1:
# xorof2 = 5 ^ 6 = 3
# Step 2:
# setbit = rightmost set bit of 3 → 1

# Step 3:
# Split into groups:
# | Group 1 (bit=1) | Group 2 (bit=0) |
# | --------------- | --------------- |
# | 3, 5, 3         | 2, 4, 2, 4, 6   |

# Step 4:
# Group 1 → 5  
# Group 2 → 6

# 🗣️ One-Line Teaching Summary
# “We use XOR to combine both odd numbers, then use a differing bit to separate them and find each one.”

# ⚠️ Important Condition
# This works only if:
# Exactly two numbers occur odd times
# Others occur even times

# ANALYSIS::
# 🧠 TIME COMPLEXITY

# Look at the loops:
# 1️⃣ First loop (XOR all elements)
# for i in range(size):
#     xorof2 ^= arr[i]
# 👉 Runs n times
# 2️⃣ Second loop (divide into two groups)
# for i in range(size):
# 👉 Again runs n times

# ⏱️ Total Time
# O(n) + O(n) = O(n)

# ✅ Final Answer:
# Time Complexity = O(n)
# ================================
# 🧠 SPACE COMPLEXITY

# Check variables used:
# xorof2, setbit, x, y
# 👉 Only a fixed number of variables, no extra data structures

# 📦 Memory used
# No extra arrays
# No recursion
# Just a few integers
# ✅ Final Answer:
# Space Complexity = O(1) (constant space)

# | Complexity | Value |
# | ---------- | ----- |
# | Time       | O(n)  |
# | Space      | O(1)  |

# “This algorithm is efficient because it finds two odd numbers in one pass style using constant memory.”

# =================================================================

# def TwoOdd(arr, size):
#   xorof2 = arr[0]
#   x = 0
#   y = 0
#   SetBit = 0
#   for i in range(1,size):

#     xorof2 = xorof2 ^ arr[i]
#   SetBit = xorof2 & ~(xorof2-1)
#   for i in range(size):
#     if(arr[i]& SetBit):
#       x = x ^ arr[i]
#     else:
#       y = y ^ arr[i]

#   print("TwoOdd elements are",x,"&",y)

# arr = []
# arr_size = int(input("Enter the size of the array"))
# for i in range(0,arr_size):
#   z = int(input("Enter element"))
#   arr.append(z)

# print("TwoOdd")