# https://codeforces.com/problemset/problem/281/A

a = input()
b = list(a)

b[0] = b[0].upper(); #just discoverd accidentally that adding ";" at the end of any statement in python doesn't throw an error because it it knows their ancestors behaviour 🤣🤣🤣

a = "".join(b)
print(a)