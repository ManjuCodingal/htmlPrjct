# OneAlgoThreeFaces - Demonstration of Time Complexity

# Function 1: Formula method (O(1))

# This directly uses a mathematical formula.
# Number of steps: Always 1 step (just multiply, add, and divide).
# Time Complexity: O(1) (constant time, no matter how big n is).
# Space Complexity: O(1).
def fun1(n):
  return n*(n+1)/2   # Direct formula
print(fun1(4))


# Function 2: Loop method (O(n))

# This adds numbers using a loop.
# For n=4 → does 4 iterations.
# In general → does n iterations.
# Time Complexity: O(n) (grows linearly with n).
# Space Complexity: O(1).
def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i


# Function 3: Nested loop method (O(n^2))

# This uses a nested loop (loop inside another loop).
# For n=4:
# → 1 + 2 + 3 + 4 = 10 iterations.
# In general → does about n(n+1)/2 ≈ n²/2 iterations.
# Time Complexity: O(n²) (quadratic growth).
# Space Complexity: O(1).
def fun3(n):
    sum = 0
    for i in range(1, n+1):
      for j in range(i, i+1):
        sum += 1
      return sum
    

# Summary of the 3 functions
# Fun1: O(1) → Best & Fastest (formula method).
# Fun2: O(n) → Medium (loop method).
# Fun3: O(n²) → Slowest (nested loops).


# ==============================
# Main program to test functions
# ==============================
if __name__ == "__main__":
    n = 4  # You can change this value

    print("Input n =", n)
    print("Fun1 result:", fun1(n), " | Time Complexity: O(1)")
    print("Fun2 result:", fun2(n), " | Time Complexity: O(n)")
    print("Fun3 result:", fun3(n), " | Time Complexity: O(n^2)")

    print("\nOrder of Growth Hierarchy:")
    print("O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)")    
# fun1 → uses the direct formula → runs in constant time O(1).
# fun2 → sums numbers with a loop → runs in linear time O(n).
# fun3 → nested loop → runs in quadratic time O(n²).    