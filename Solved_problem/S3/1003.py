"""
0 / 1 0
1 / 0 1
2 / 1 1
3 / 1 2
4 / 2 3
5 / 3 5
6 / 5 8
7 / 8 13
"""
t = int(input())
for i in range(t):
    a = int(input())
    m1 , m2 = 1,0
    x,y = 1, 0
    
    for j in range(1,a+1):
        m1 = y
        m2 = x+y
        x = m1
        y = m2  
    print(m1,m2)
    
            