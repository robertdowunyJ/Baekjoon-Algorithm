import sys
input = sys.stdin.readline

a = list(map(int , input().split()))
sum_val = 0

for i in range (5):
    sum_val += a[i]**2

uniq = sum_val %10

print(uniq)