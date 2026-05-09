s = "abc"
n = len(s)

for i in range(1, 1 << n):  
    sub = ""
    for j in range(n):
        if i & (1 << j):
            sub += s[j]
    print(sub)