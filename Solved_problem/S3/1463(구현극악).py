n= int(input())

lst = [i for i in range(1,n+1)]
cnt_lst=[]

for i in range(n):
    if i == 0:
        cnt_lst.append(0) #일단 1의 위치에 0번 연산 임을 첨가
    elif i == 1:
        cnt_lst.append(1)
    elif i == 2:
        cnt_lst.append(1)
    else:
        tmp = []
        if (i+1) % 3 == 0:
            s = cnt_lst[(i+1)//3-1]+1 #만약 i =5 , 6이라는 얘의 값을 판단하려고해, 
            tmp.append(s) 
        if (i+1) % 2 == 0:
            s = cnt_lst[(i+1)//2-1]+1 
            tmp.append(s)
        s = cnt_lst[i-1] +1
        tmp.append(s)
        cnt_lst.append(min(tmp))
    #여기까지 최소 횟수 tmp 리스트에 추가해놓고, 작은거 가져오기
    

print(cnt_lst[n-1])
            