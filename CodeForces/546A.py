# https://codeforces.com/problemset/problem/546/A

a = list(map(int, input().split()))
b = a[0] * int(a[2] * (a[2] + 1) / 2)

if b > a[1]: print(b - a[1])
else: print(0)