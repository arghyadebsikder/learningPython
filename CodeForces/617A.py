# https://codeforces.com/problemset/problem/617/A

a = int(input())
b = 0

for i in range(5, 0, -1):
    if a >= i: 
        b += int(a / i)
        a %= i
        # print(a, i)
    
print(b)