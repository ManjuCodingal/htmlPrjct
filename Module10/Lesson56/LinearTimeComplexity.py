# Program to show linear time complexity(O(n)) by entering any nn.
def onTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("when n is ", n, "iteration= ", iteration)

onTime(25)
onTime(56)
print("with every n the time taken and iterations will increase.")
    