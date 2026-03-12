n = int(input())

lst = list(map(int,input().split()))

max_num = max(lst)

for i in range(n):
    lst[i] = lst[i]/max_num *100
    
avg = sum(lst) / n

print(avg)