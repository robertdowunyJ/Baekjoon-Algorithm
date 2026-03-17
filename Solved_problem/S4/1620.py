import sys
input = sys.stdin.readline

n ,m = map(int,input().split())

lst = []
my_dict = dict()
cnt = 1

for i in range(n):
    name = input().strip()
    lst.append(name)
    my_dict[name] = cnt
    cnt+=1


for i in range(m):
    question = input().strip()
    if question.isdigit():
        print(lst[int(question)-1])
    else:
        print(my_dict[question])
