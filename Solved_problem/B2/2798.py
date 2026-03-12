n,m = map(int,input().split())
lst = list(map(int,input().split()))


result=0
max_result = 0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            result = lst[i]+lst[j]+lst[k]
            
            if max_result < result and result <= m:
                max_result = result


print(max_result)