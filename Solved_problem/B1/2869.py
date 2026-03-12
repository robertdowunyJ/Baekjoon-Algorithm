a,b,v = map(int,input().split())

days_per_up = a-b



#더해주고 빼주면 1씩올라갈떄, 높이가 높으면 엄청오래걸리겠네
#두개의 차이를 나누기 연산으로 할까?
result = 0
if (v-a) % days_per_up == 0:
    result = (v-a)//(a-b)+1
    print(result)
else:
    print((v-a)//(a-b) + 2)

    