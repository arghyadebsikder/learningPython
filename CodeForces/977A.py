# https://codeforces.com/problemset/problem/977/A

a = list(map(int, input().split()))
b = a[0]
c = a[1]

for i in range(c):
    if b % 10 == 0:
        b /= 10
    else: b -= 1
    
print(int(b)) 