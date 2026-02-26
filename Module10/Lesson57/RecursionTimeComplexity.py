# Calculate the time complexity of the recursive function.
# T(n)=T(n/2)+T(n/2)
# here the recursion function will take 2 recursive calls and rest of the code will take a constant time.
def myFunc(n):
    if n<=0:
        return
    print("codingal") #Constant extra work
    myFunc(n//2)#recursive call1
    myFunc(n//2)#recursive call2
    
myFunc(8)
#recurence relations will be
# T(n)=T(n/2)+T(n/2)+ O(1)    ie. O(1) as constant time.
# Two recursive calls and a Constant extra work



#     Tree View
#         8                    1 call
#       /   \
#      4     4                 2 call
#     / \   / \
#    2  2  2  2                4 call
#   /\
#  1 1 ...                     8 call

# Level 1 → 1 call
# Level 2 → 2 calls
# Level 3 → 4 calls 
# Level 4 → 8 calls …   ie.Calls double each level.

# here the number of calls is like 1,2,4,8,16 that is multiplying by 2 at each level.That is Exponential growth.
#height of tree =log n.
# Time Complexity = O(n)
# When recursion splits into two halves repeatedly → total work becomes linear.