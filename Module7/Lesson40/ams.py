x = int(input("Enter a number to detect your armstrong number...: "))
y = len(str(x))
print(f"Your number has {y} digits")
z = 0
for digit in str(x):
    z = z + int(digit) ** y
if z == x:
    print(f"{x} is an armstrong number.")
else:
    print(f"{x} is not an armstrong number.")