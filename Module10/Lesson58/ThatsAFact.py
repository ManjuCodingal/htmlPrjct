# To find factors of user input
 
# Goes from 1 to number and checks if I divide the number. If yes, it is a factor
def print_factors(number):
   print("The factors of",number,"are:")
   for i in range(1, number + 1):
       if number % i == 0:
           print(i)
 
# Taking input from the user
number = int(input("Enter your number to find it's factors: "))
 
# Calling our function
print_factors(number)


# number = int(input("Input number:"))
# s = 0
# temp = number

# while temp!=0:
#   digit = temp%10
#   s = s+digit**3
#   temp = temp//10
# if number == s:
#   print(number, "is an armstrong number ")
# else:
#   print(number, "is not an armstrong number ")