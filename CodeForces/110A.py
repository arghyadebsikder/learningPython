# https://codeforces.com/problemset/problem/110/A

a = int(input())
b = 0
c = True

while a > 0:
    if a % 10 == 4 or a % 10 == 7:
        b += 1
    a = int(a / 10)
    
while b > 0:
    if b % 10 == 4 or b % 10 == 7:
        c = c
    else: c = False
    b = int(b / 10)
    
if c:
    print("YES")
else: print("NO")

# print(int(9.9))