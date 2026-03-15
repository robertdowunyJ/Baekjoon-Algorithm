import sys
input = sys.stdin.readline

n = int(input())

count = [0]*10001

for i in range(n):
    a = int(input())
    count[a]+=1

# 0 2 2 2 1 2 

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
