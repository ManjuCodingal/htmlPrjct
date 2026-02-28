# Program to find the number of zero bits and one bits present in a number
 
# Functions taking our number as input 
def numberOfBits(n):
    ones = 0
    zeros=0
    
    # while our number is grater than zero check last bit and right shift
    while (n):
        
        # use AND operator to check if last bit is 1 or 0
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        # Right shift the number remove the last bit that we just checked above
        n >>= 1
    print("\n\nOnes = ",ones,"\nZeros ",zeros)
 
 
number = int(input("Enter your number : "))
numberOfBits(number)


# def numberOfBits(n):
#   ones = 0
#   zeroes= 0
#   while (n):
#       if (n & 1 == 1):
#           ones += 1
#       else:
#           zeroes += 1
#       n >>= 1
#   print("Number of ones =", ones, "\nNumber of zeroes =", zeroes)

# number = int(input("Enter your number: "))
# numberOfBits(number)