N=int(input())
cnt = 0
dp = [0]*(N+1)
#dp인덱스의 값은 최소 횟수임
sqr = [x*x for x in range(1,224)]

if N == 1:
    print(1)
elif N == 2:
    print(2)
elif N >= 3:
    dp[1] = 1
    dp[2] = 2
    for i in range(3,N+1):
        T = i**0.5
        if T % 1 == 0: #시간초과나면 정수인지 판별하는함수
            dp[i] = 1 #제곱수이면 1로
        else: #11339 = 106^2 +...
            k = int(T) #106
            min_dp = 4
            for sq in sqr:
                if dp[i-sq] == 1 and sq < i:
                    dp[i] = dp[i-sq]+1
                    break
                else:
                    if dp[i-sq]+1 < min_dp:
                        min_dp = dp[i-sq]+1
                dp[i] = min_dp
            # for j in range(k): #106에서 1씩줄여가며 빼봐서 dp값 비교
            #     if dp[i-(k-j)**2]+1 < min_dp: #N에서 106제곱수 빼고 
            #         min_dp = dp[i-(k-j)**2]+1
            # dp[i] = min_dp
    print(dp[N])