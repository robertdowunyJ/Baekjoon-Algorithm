import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n ==0 :
        break
    lst = list(map(int,str(n)))
    k = len(lst)//2
    cnt = 0
    for i in range(k):
        if lst[i] == lst[len(lst)-1-i]:
            cnt+=1
            continue
    if cnt == k:
        print("yes")
    else:
        print("no")
        