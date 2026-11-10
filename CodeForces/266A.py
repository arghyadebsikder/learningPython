# https://codeforces.com/problemset/problem/266/A

a = int(input())
b = list(input())
i = 0
    
while i in range(len(b) - 1):
    if b[i] == b[i + 1]:
        b.pop(i)
    else: i += 1
        
        
print(a - len(b))

