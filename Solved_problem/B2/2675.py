T = int(input())

for i in range(T):
    lst = list(input().split()) # 3 abc 입력
    k = int(lst[0]) # k에 3 저장
    lst_S = list(lst[1].strip()) #lst_s에 abc 각각 저장
    for j in range(len(lst_S)): #3번씩 반복
        print(lst_S[j]*k,end='') 
    print()