# 🔹 What is a Set Bit?
# A set bit = a bit that is 1
# An unset(not set)  bit = a bit that is 0

# Program to check if the Nth bit is set or not 
 
def setOrNot(number, n):
 
    # Make a mask variable by left shifting 1 (k-1) times and check if (n AND mask) equals 1 or 0
    if number & (1 << (n - 1)):
        print( "\nSET")
    else:
        print("\nNOT SET")
 
 
number = int(input("Enter number : "))
n = int(input("Enter bit number : "))
setOrNot(number, n)

# Example:
# number = 6   # 0110
# n = 1

# Mask: (left shift)
# 1 << 0 = 0001

# AND:
# 0110
# 0001
# ----
# 0000

# So, ❌ Output: NOT SET (If result = 1 → SET, else → NOT SET)


# =======================================================
# def setOrNot(number, n):
#   # You need to define 'mask' before using it
#   mask = 1  # Assuming you want to check if the bit is set or not 
#   if (n & mask) == 1 or (n & mask) == 0:  # Corrected comparison and OR operator
#     if number & (1 << (n - 1)):
#       print("SET")
#     else:
#       print("NOT SET")
# number = int(input("Enter the number: "))
# n = int(input("Enter the bit position: "))
# setOrNot(number, n)