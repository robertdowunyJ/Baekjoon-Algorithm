n = int(input())
lst = list(map(int,input().split()))
T,P = map(int,input().split())


T_bundle = 0
for i in range(len(lst)):
    if lst[i] != 0 and lst[i]%T != 0:
        T_bundle = T_bundle + lst[i]//T +1
    elif lst[i] != 0 and lst[i]%T == 0:
        T_bundle = T_bundle + lst[i]//T
print(T_bundle)
print(n//P,n%P)