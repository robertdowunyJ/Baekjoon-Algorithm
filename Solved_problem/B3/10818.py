import sys
input = sys.stdin.readline

max_num = -1000000
min_num = 1000000

n = int(input())

lst = list(map(int,input().split()))

for i in range(n):
    if max_num < lst[i]:
        max_num = lst[i]
    if min_num > lst[i]:
        min_num = lst[i]

print(min_num , max_num)
