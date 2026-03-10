a,b= map(int,input().split())

#각 약수를 리스트에 추가, 합집합, 최댓값 
lst_a =[]
lst_b =[]
for i in range (1,a+1):
    if a % i == 0:
        lst_a.append(i)
for i in range (1,b+1):
    if b % i == 0:
        lst_b.append(i)

s1 = set(lst_a)
s2 = set(lst_b)
s = s1 & s2

lst_c=[]
lst_d=[]
k = max(s)
print(k)

print(k*(a//k)*(b//k))    