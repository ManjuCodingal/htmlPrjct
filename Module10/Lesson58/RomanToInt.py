# Program to convert roman numerals to integers
 
def romanToInt(romanInput):
 
    # All roman units with integer equivalent values
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
 
    #  result
    resultInteger = 0
 
    # Go from 0 to len-1 if integer equivalent is greater than next element then add it else subtract it
 
    for i in range(0, len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]      
    return resultInteger + roman[romanInput[-1]]
 
# Take roman as input from user
roman = input("Input roman numeral : ")
 
# Print the integer
print("Integer equivalent : ",romanToInt(roman))


# def roman_to_int(a):
#   roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#   int_form=0
#   for i in range(len(a)):
#     if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:
#       int_form-=roman[a[i]]
#     else:
#       int_form+=roman[a[i]]
#   return int_form

# a=input("enter a roman numeral")
# print("interger form of",a,"is",roman_to_int(a))