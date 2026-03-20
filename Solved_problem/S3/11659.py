import sys
input = sys.stdin.readline
n,m = map(int,input().split())

lst = list(map(int,input().split()))

sum_list = []
sum_val = 0

for _ in range(m):
    k,j = map(int,input().split())
    for i in range(0,n+1):
        if i == 0:
            sum_list.append(sum_val)
            continue
        sum_val = sum_val + lst[i-1]
        sum_list.append(sum_val)
    print(sum_list[j] - sum_list[k-1])
