#  https://codeforces.com/problemset/problem/236/A

a = input()
c = 0;

for i in range(len(a)):
    b = True;
    for j in range(i):
        if a[i] == a[j]: b = False;
    if b == True: c += 1

if c % 2 == 0: print("CHAT WITH HER!")
else: print("IGNORE HIM!")
