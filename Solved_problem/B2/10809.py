lst = [-1 for _ in range(26)]

s = list(input().strip())
cnt = 0
for char in s:
    idx = ord(char)-ord('a') #b가 나타난곳이 idx 1번이고 , b의 위치는 0번째
    if lst[idx] == -1:
        lst[idx] = cnt
    cnt+=1

for i in range(26):
    print(lst[i],end=' ')  
 