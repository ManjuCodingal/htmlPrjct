# Program to check if a number is the power of 2
  
def power2(number):
    
    # As the power of 2 will have only 1 set bit, then n-1 & n will always be 0 for any power of 2
    if (number == 0):
        return 0
    if ((number & (~(number - 1))) == number):
        # (number & (~(number - 1))) == number.
        # This works because it isolates the lowest set bit, but it's not the most common or readable way to check for powers of 2.

        # number - 1
        # Subtracting 1 flips bits from the rightmost set bit onward. 
# Example:
# number = 8  → 1000
# number-1 = 7 → 0111

# ~(number - 1) (bitwise NOT)
# This inverts all bits:
# number-1 = 0111
# ~(number-1) = 1000   (ignoring leading bits for simplicity)

# number & (~(number - 1))
# This keeps only the lowest set bit of number.
# Example:
# number = 1000
# ~(number-1) = 1000
# AND result = 1000

# number & (~(number - 1))
# 👉 isolates the rightmost (lowest) set bit of the number.

# (number & (~(number - 1))) == number
# This checks:
# If the number has only one set bit, then isolating the lowest set bit gives the same number.
# That means → it's a power of 2.

        return 1
    return 0
  
number = int(input("Enter the number : "))
 
if(power2(number)):
    print("\nThe number is power of 2")
else:
    print("\nThe number is not power of 2")
 

# ⚡ Time Complexity
# All operations (&, ~, -) are bitwise operations
# They run in constant time
# 👉 Time Complexity: O(1)

# 💾 Space Complexity
# No extra memory used
# Only a few variables
# 👉 Space Complexity: O(1)


# def power2(number):
#   if number <= 0:
#       return False
#   return (number & (number - 1)) == 0

# n = int(input("Enter a number: "))
# if power2(n):
#     print("\nThe number is a power of 2")
# else:
#     print("\nThe number is not a power of 2")