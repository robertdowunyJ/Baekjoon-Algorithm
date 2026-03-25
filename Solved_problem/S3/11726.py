"""
1일때, = 1
2일때 2
3일떄 , 3
4일때, 5
5일때, 8
6일때, 13
7일때 ,21
8일때, 34
9일때, 55
n일때, lst[n-2]+lst[n-1]
"""


#lst = [1,2,3,5,8,13,21,34,]
n= int(input())

lst=[]
lst.append(1) 
lst.append(2)
for i in range(2,n):
    lst.append(lst[i-1]+lst[i-2])

print(lst[n-1]%10007)


