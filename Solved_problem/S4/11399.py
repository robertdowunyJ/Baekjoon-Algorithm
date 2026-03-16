n = int(input())

lst = list(map(int,input().split()))

total = 0
lst.sort()

for i in range(n):
    total = total + lst[i]*(n-i)

print(total)