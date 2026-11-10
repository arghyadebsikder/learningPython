# https://vjudge.net/contest/779451#problem/D
# https://cses.fi/problemset/task/1070

a = int(input())
b = [0] * a;
# print(b[1])

if a > 1 and a < 4: print("NO SOLUTION")
elif a == 4: print(2, 4, 1, 3)
else:
    a += 1
    j = 0;
    for i in range(1, a, 2):
        b[j] = i
        j += 1
    for i in range(2, a, 2):
        b[j] = i
        j += 1
    
    b = " ".join(map(str, b))
    print(b)



# 1. 1
# 2. x
# 3. x
# 4. x
# 5. 1, 3, 5, 2, 4
# 6. 1, 3, 5, 2, 4, 6
# 7, 1, 3, 5, 7, 2, 4