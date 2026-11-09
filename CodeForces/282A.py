# https://codeforces.com/problemset/problem/282/A

a = int(input())
x = 0

for i in range(a):
    b = input()
    if b[1] == '+': x += 1
    else: x -= 1
    
print(x)