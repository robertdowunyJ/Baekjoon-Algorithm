import sys
input = sys.stdin.readline

n=int(input())
for _ in range(n):
    test_case = int(input())
    result = 1
    my_dict = dict()
    for i in range(test_case):
        name,wear = input().split()
        if wear not in my_dict: 
            my_dict[wear] = 1
        else:
             my_dict[wear] +=1
    for value in my_dict.values():
        result *= (value+1)
    print(result-1)

