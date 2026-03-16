n, k =map(int,input().split())

result = n
r = 1
for i in range(k-1):
    result = result * (n-1)
    n -=1

for i in range(2,k+1):
    r = i*r

if k == 0:
    print(1)
else:
    print(result//r)