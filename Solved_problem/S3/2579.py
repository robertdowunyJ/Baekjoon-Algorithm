import sys
input = sys.stdin.readline

n = int(input())
lst=[]
for _ in range(n):
    s = int(input())
    lst.append(s)

#뭔가 예시를 쉽게 들수가 없네 문제 조건에 충실해서 그냥 구현해야겠네 dp문제같네 시간1초

#끝에서 출발하는것이 0번째라고한다면, 경우의 수는 (0,1,3),(0,2,3),(0,2,4) =>최댓값 채택, ->  

dp=[]

if n == 1:
    print(lst[0])
elif n == 2:
    print(lst[0]+lst[1])

elif n >=3:
    dp.append(lst[0])
    dp.append(lst[1]+lst[0])
    dp.append(max(lst[0]+lst[2],lst[1]+lst[2]))

    for i in range(3,n):
        dp.append(max(dp[i-2]+ lst[i] , dp[i-3]+lst[i-1]+lst[i]))
    print(dp[n-1])