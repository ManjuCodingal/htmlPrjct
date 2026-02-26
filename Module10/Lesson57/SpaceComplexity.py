# Calculate the space complexity of the recursive function.

#METHOD 1
def sum_n(n):
    return n * (n + 1) // 2 # integer result
print("Sum of first n numbers (n=5):", sum_n(5))

#METHOD 2
def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total
# Examples
a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))

#METHOD 3
def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)
print("Recursive sum (n=5):", summ(5))

#METHOD1 
# NO recursion no loop only one calculation.
# Space=O(1) ie.constant memory

#METHOD2
#as the array size grows memory grows.
#Space complexity = O(n)
#Auxillary space= O(1)
#no recursion

#METHOD3
#that is recursive function.
#space complexity= O(n), uses extra space.
#time complexity= O(n)