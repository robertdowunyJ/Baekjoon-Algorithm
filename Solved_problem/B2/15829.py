n = int(input())
string = input()
cnt=0
result = 0
for char in string:
    result +=(ord(char)-ord('a') + 1)*31**(cnt)
    cnt +=1


result = result % 1234567891

print(result)