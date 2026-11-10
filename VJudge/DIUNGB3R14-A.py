# https://vjudge.net/contest/779451#problem/A
# https://codeforces.com/problemset/problem/1454/A

def f():
    a = int(input())
    print(a, end="")
    for i in range(1, a):
        print(f" {i}", end="")    
    print("")
    
    
z = int(input())
while z:
    f()
    z -= 1
    
    
 