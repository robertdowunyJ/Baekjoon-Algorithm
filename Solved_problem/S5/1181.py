import sys
sys.stdin.readline

n = int(input())
lst = dict()

for i in range(n):
    a = input().strip()
    k = len(a)
    lst[a] = k

sorted(lst.items(),key=lambda x:x[1])
print(lst)         
    