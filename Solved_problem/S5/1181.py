import sys
input = sys.stdin.readline

n = int(input())
lst = dict()

for i in range(n):
    a = input().strip()
    k = len(a)
    lst[a] = k

lst = sorted(lst.items(),key=lambda x:(x[1],x[0]))
for word,length in lst:
    print(word)      
    