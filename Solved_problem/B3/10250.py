import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    H,W,N=map(int,input().split())
    y = N % H
    x = N//H +1
    print(str(y)+str(x).zfill(2))
        
    