x = int(input("How many terms of the Fibonacci series would you like? "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")

while count < x:
    print(a, end=" ")
    a, b = b, a + b
    count += 1