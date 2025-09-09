file1 = input("What is the file you want to import to?")
file2 = input("What is the file you want to import to for the first file?")
f1 = open(file1, 'r')
f2 = open(file2, 'r')
print("This is your file of students and their fav subjects before you handled them with the 2nd file", f1.read())
print("This is your file of students and their fav subjects of the 2nd file", f2.read())
f1.close()
f2.close()
f1 = open(file1, 'a+')
f2 = open(file2, 'r')
f1.write(f2.read())
f1.seek(0)
f2.seek(0)
print("Now your students are", f1.read())
print("Your 2nd file is", f2.read())
f1.close()
f2.close()

# or

# file1 = input("What is the file you want to import to? ")
# file2 = input("What is the file you want to import from (the second file)? ")

# # Read initial contents
# with open(file1, 'r') as f1, open(file2, 'r') as f2:
#     file1_contents = f1.read()
#     file2_contents = f2.read()

# print("\nThis is your file of students and their favorite subjects BEFORE merge:")
# print(file1_contents)

# print("\nThis is your 2nd file of students and their favorite subjects:")
# print(file2_contents)

# # Append contents of file2 to file1
# with open(file1, 'a') as f1:
#     f1.write(file2_contents)

# # Show updated contents of file1
# with open(file1, 'r') as f1:
#     updated_file1_contents = f1.read()

# print("\nNow your students are:")
# print(updated_file1_contents)

# # Re-read file2 to show it's unchanged
# with open(file2, 'r') as f2:
#     print("\nYour 2nd file is still:")
#     print(f2.read())
