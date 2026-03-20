import sys
input = sys.stdin.readline
n,m = map(int,input().split())

lst = list(map(int,input().split()))

sum_val = 0

for s in range(m):
    k,j = map(int,input().split())
    sum_val = lst[0]
    if s == 0:
        for i in range(1,n):
            sum_val = lst[i-1]+lst[i] #lst[0]+lst[1]
            lst[i] = sum_val

    if k == 1:
        print(lst[j-1])
    else:
        print(lst[j-1]-lst[k-2])
    ##lst 업뎃됨..?
