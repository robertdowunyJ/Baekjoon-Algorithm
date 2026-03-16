cnt_0 = 0
cnt_1 = 0

def fibonacci(n):
    if n == 0:
        cnt_0 +=1
        return 
    elif n ==1:
        cnt_1 +=1
        return
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    


t = int(input())

for i in range(t):
    a = int(input())
    fibonacci(a)
    print(cnt_0,cnt_1)
    cnt_0 = 0
    cnt_1 = 0
