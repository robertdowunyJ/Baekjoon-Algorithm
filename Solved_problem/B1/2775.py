"""def room(k,n):
    if k==0 or n ==1:
        return n
    return room(k-1,n)+room(k,n-1)
"""

T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    lst = list(range(1,n+1)) #[1,2,3,4,5,...14]

    for i in range(k):#14층까지 14번 반복
        for j in range(1,n):
            lst[j] += lst[j-1] 
    print(lst[n-1])
     

#처음맛보는 DP, 시간초과의 늪.. 재귀가 모든 시간초과를 해결해주지않는다