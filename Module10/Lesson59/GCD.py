numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))
while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is: ", numberLargest)

# The code finds the HCF/GCD using the Euclidean Algorithm. 

# The Euclidean Algorithm is a standard method in Number Theory for computing the Greatest Common Divisor (GCD), also called HCF (Highest Common Factor).
# The algorithm repeatedly calculates the remainder.
# 48 % 18 = 12
# 18 % 12 = 6
# 12 % 6  = 0
# When the remainder becomes 0, the current largest value is the GCD/HCF.
# HCF = 6