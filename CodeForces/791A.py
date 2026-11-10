# https://codeforces.com/problemset/problem/791/A

a = list(map(int, input().split()))

for i in range(9999999):
    if(a[0] > a[1]):
        print(i)
        break
    a[0], a[1] = a[0] * 3, a[1] * 2