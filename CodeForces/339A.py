# https://codeforces.com/problemset/problem/339/A

import math

a = input()
arr = [0] * (int(math.ceil(len(a) / 2)))

for i in range(len(arr)):
    arr[i] = a[i * 2]

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]: arr[i], arr[j] = arr[j], arr[i]
        
a = "+".join(arr)
print(a)

# for i in range(len(arr)):
#     print(arr[i], end = "")
#     print("+" if i < len(arr) - 1 else "\n", end = "")
    

    