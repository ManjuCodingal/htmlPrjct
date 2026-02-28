def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

    for p in range(2, num+1):
        if prime[p]:
            print(p)

num = int(input("Enter a number"))
print("Following are the prime numbers smaller")
print("than or equal to", num)
SieveOfEratosthenes(num)

# def primeSeive(n):
#     prime = [True for i in range(n + 1)]
#     currentNumber = 2
#     while (currentNumber * currentNumber <= n):
#         if (prime[currentNumber] == True):
#             for i in range(currentNumber ** 2, n + 1, currentNumber):
#                 prime[i] = False
#         currentNumber += 1
#     prime[0]= False
#     prime[1]= False
#     for p in range(n + 1):
#         if prime[p]:
#             print(p)


# n = int(input("Enter number to find all prime numbers less than the number : "))
# primeSeive(n)
# print ("Following are the prime numbers smaller.")
# print ("than or equal to")
