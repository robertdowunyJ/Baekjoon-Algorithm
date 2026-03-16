import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lst_n = []
lst_m = []
for i in range (n):
    a = input().strip()
    lst_n.append(a)

for i in range (m):
    a = input().strip()
    lst_m.append(a)

s = set(lst_n) & set(lst_m)


print(len(s))
s = list(s)
s.sort()

for i in range(len(s)):
    print(s[i])

    