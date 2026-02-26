# Calculate the space complexity of the recursive function.

#METHOD 1 : formula sum of first n numbers
def sum_n(n):
    return n * (n + 1) // 2 # integer result
print("Sum of first n numbers (n=5):", sum_n(5))

#METHOD 2 : Loop array sum
def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total
# Examples
a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))
# Loop runs once for each element
# If array has n elements → n steps

#METHOD 3 : Recursive sum of first n numbers
def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)
print("Recursive sum (n=5):", summ(5))
# summ(5) → 5 + summ(4)
# summ(4) → 4 + summ(3)
# summ(3) → 3 + summ(2)
# summ(2) → 2 + summ(1)
# summ(1) → 1 + summ(0)
# summ(0) → stop (base case)
# Each recursive call stays in memory (call stack).

# summ(5)
# summ(4)
# summ(3)
# summ(2)
# summ(1)
# That is 5 stack frames.

# -------Analysis of Space Complexity-------

# METHOD1 
# NO recursion no loop only one calculation.
# Space=O(1) ie.constant memory
# O(1) time

# METHOD2
#as the array size grows memory grows.
# Space complexity = O(n) ie.input space
# Time Complexity = O(n)
# Auxillary space= O(1) ie.extra space used by the algorithm.
#no recursion

# METHOD3
# that is recursive function.
# space complexity= O(n), uses extra space.
# time complexity= O(n)

# Example Use in real coding?
# METHOD1, Formula sum	⭐ Best, Fast, constant memory
# METHOD2, Loop array sum	⭐ Very common, Practical
# METHOD3, Recursive sum	⚠️ Rare, Uses extra memory