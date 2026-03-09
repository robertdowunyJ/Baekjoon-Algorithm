import sys

input = sys.stdin.readline

n = int(input())
plus_point = 0
total = 0
#경우의수 oo ox xo xx

for i in range(n):
    score = list(input().strip())
    for j in range(len(score)):
        if j == 0 and score[j] == 'O': 
            total +=1
        elif j!= 0 and score[j] == 'O' and score[j-1] == 'O':
            plus_point +=1
            total = total + 1 + plus_point
        elif j!= 0 and score[j] == 'X' and score[j-1] == 'O':
            plus_point = 0
        elif j!= 0 and score[j] == 'O' and score[j-1] == 'X':
            total +=1
    print(total)
    total = 0
    plus_point = 0
    
"""
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    score = input().strip() # 리스트로 안 만들고 문자열 그대로 써도 됩니다
    
    total = 0  # 총점
    combo = 0  # 연속 점수 (누적 보너스)
    
    for char in score: # 인덱스 j 필요 없이 글자 하나씩 꺼내기
        if char == 'O':
            combo += 1      # 콤보 증가 (1 -> 2 -> 3...)
            total += combo  # 총점에 콤보만큼 더하기
        else:
            combo = 0       # X 만나면 콤보 초기화
            
    print(total)
    
"""