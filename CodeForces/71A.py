# https://codeforces.com/problemset/problem/71/A

a = int(input())
for i in range(a):
    b = input()
    if len(b) > 10: print(str(b[0]) + str(len(b) - 2) + str(b[len(b) - 1]))
    else: print(b)