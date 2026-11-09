# https://codeforces.com/problemset/problem/263/A

for i in range(5):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        if a[j] == 1:
            b = i
            c = j

print(abs(b - 2) + abs(c - 2))