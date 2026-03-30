# Program to check if a number is power of 4
 
def powerOf4(number):
     
    count = 0
     
    # If only 1 set bit exists
    if (number & (~(number & (number - 1)))):
         
        # Count 0 bits before set bit
        while(number > 1):
            number >>= 1
            count += 1
         
        # If count is even return true else false
        if(count % 2 == 0):
            return True
        else:
            return False
 
 
number = int(input("Enter your number : "))
if(powerOf4(number)):
    print(number, 'is a power of 4')
else:
    print(number, 'is not a power of 4')

# A number is a power of 4 if:
# It has only one set bit (i.e., it's a power of 2)
# The position of that set bit is even (0-based index)

# Check if number has only one set bit
# if (number & (~(number & (number - 1)))):
# What this does:
# number & (number - 1) removes the lowest set bit
# If result is 0, it means only one set bit exists
# What this does:
# number & (number - 1) removes the lowest set bit
# If result is 0, it means only one set bit exists
# 👉 Example:
# 8 = 1000
# 7 = 0111
# 8 & 7 = 0000 → only one set bit
# ~(...) flips bits
# number & ~(...) ensures we isolate that set bit
# ✔️ So this condition ensures the number is a power of 2

# Count number of shifts (position of set bit)
# while(number > 1):
#     number >>= 1
#     count += 1
# Right shift divides number by 2 each time
# count becomes the position of the set bit
# 👉 Example:
# 16 → 8 → 4 → 2 → 1
# count = 4

# Check if position is even
# if(count % 2 == 0):
# Powers of 4 have set bits at positions:
# 1  → position 0
# 4  → position 2
# 16 → position 4
# ✔️ All even positions

# ⏱️ Time Complexity
# Breakdown:
# Bitwise check → O(1)
# While loop → runs log₂(n) times
# 👉 Final Time Complexity:
# O(log n)

# 💾 Space Complexity
# Only a few variables (count, number)
# No extra data structures
# 👉 Space Complexity:
# O(1)