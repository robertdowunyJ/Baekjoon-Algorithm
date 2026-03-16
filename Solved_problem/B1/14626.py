lst = list(input().strip())

result = 0
f = 0
for i in range(13):
    if i % 2 == 0 and lst[i] != '*':
        result = result + int(lst[i])
    elif i % 2 == 1 and lst[i] != '*':
        result = result + int(lst[i])*3
    if lst[i] == '*':
        k=i
    # *에 들어갈 숫자까지 규칙 적용해서 더한다음 
    # 10으로 나누면 lst[12]의 값이 나온다
for j in range(10):
    if k % 2 == 0:
        if (result+f)%10 == 0:
            break
    elif k % 2 == 1:
        if (result + f*3)%10 == 0:
            break
    f+=1

print(f)

