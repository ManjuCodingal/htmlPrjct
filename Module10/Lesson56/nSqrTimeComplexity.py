# Program to show time complexity(O(n^2)) by entering any n.
def onSquareTime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end=" ")
            iteration+=1
        print(" ")
    print("when n is ", n, "iterations= ", iteration)
    
onSquareTime(5)
onSquareTime(4)
onSquareTime(3)

print("with every n the time taken= n Square.This is order of n Square")