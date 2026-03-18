import sys
input = sys.stdin.readline
n,k=map(int,input().split())
lst =[]
cnt=0
for i in range(n):
    a = int(input())
    lst.append(a)

for i in range(n): # k = 4200
    if k // lst[n-1-i] > 0:
        cnt += k // lst[n-1-i]
        k -= lst[n-1-i] * (k // lst[n-1-i])

print(cnt)
