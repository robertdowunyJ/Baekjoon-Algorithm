n= int(input())
cnt =0
power_2 = 0
while True:
    k = n
    while True:
        if k % 2 == 1 and k != 1: #k를 2로 나누었을때 안나눠짐, 또는 
            power_2 = 0
            break
        elif k % 2 == 0 and k != 1:
            k = k//2 #8-4-2-1
            power_2 +=1
        elif k == 1:
            break
    #2의 거듭제곱이면 k = 1임/ 아니면 그냥 n으로 계산 (백만이니까 해봤자 19번까지밖에 계산안함)

    if k == 1 or n == 1:
        break

    else:
        if n % 3 == 0:
            n = n//3
            cnt +=1
            continue
        elif n % 3 == 1:
            n -= 1
            cnt +=1
            continue
        else:
            n -=1
            cnt +=1
            continue

print(cnt+power_2)
