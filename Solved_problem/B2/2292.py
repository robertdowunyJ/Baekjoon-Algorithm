#1, 
# 2~7, 6개
#  8~19, 12개
# 20~37 18개
#계차수열?
#사이의 값일텐데, 어떻게 찾지
#1 + 6 + 12 + 18 + 24 + 30 + ...
cnt = 1
k = 1
n = int(input())

while True:
    k += 6*cnt #첨에 k = 7
    if n ==1:
       print("1")
    else: 
        if n <= k:
            print(cnt+1)
            break
        else:
            cnt +=1
            continue 
        