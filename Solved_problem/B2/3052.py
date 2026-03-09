import sys
input = sys.stdin.readline

lst = []
for i in range(10):
    n = int(input())
    lst.append(n%42)
lst = set(lst)
print(len(lst))
