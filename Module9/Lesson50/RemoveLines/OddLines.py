# Program to copy odd lines of one file to another
# open file in read mode
fn = open('txtFile1.txt', 'r')

# open other file in write mode
fn1 = open('txtFile2.txt', 'w')

# read the content of the file line by line
cont = fn.readlines()
# type(cont)

# Loop through each line using 1-based indexing
for i in range(1, len(cont)+1):
	if(i % 2 != 0):  # Check for odd-numbered lines (1st, 3rd, etc.)
		fn1.write(cont[i-1])  # i-1 because list indexing starts at 0
	else:
		pass

# close the destinatn file
fn1.close()

# open file in read mode
fn1 = open('txtFile2.txt', 'r')

# read the content of the file
cont1 = fn1.read()

# print the content of the file
print(cont1)

# close all files
fn.close()
fn1.close()


