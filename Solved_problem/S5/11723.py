import sys
input = sys.stdin.readline

M = int(input())
S =[]
for i in range(M):
    lst = list(input().split())

    if lst[0] == "add":
        if lst[1] not in S:
            S.append(lst[1])
    
    elif lst[0] == "check":
        if lst[1] in S:
            print(1)
        else:
            print(0)

    elif lst[0] == "remove":
        if lst[1] in S:
            S.remove(lst[1])

    elif lst[0] == "toggle":
        if lst[1] in S:
            S.remove(lst[1])
        else:
            S.append(lst[1])

    elif lst[0] == "all":
        S = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

    elif lst[0] == "empty":
        S = []
