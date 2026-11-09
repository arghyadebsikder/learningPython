# https://codeforces.com/problemset/problem/231/A

a = int(input())
d = 0
 
for i in range(a):
    b = input()
    c = int(b[0]) + int(b[2]) + int(b[4])
    if c > 1: d = d + 1

print(d)