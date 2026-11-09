# https://codeforces.com/problemset/problem/158/A

a = list(map(int, input().split()))
b = int(a[0])
c = int(a[1])
e = 0
d = list(map(int, input().split()))

for i in range(b):
    if d[i] > 0 and d[i] >= d[c - 1]: e += 1

print(e)
