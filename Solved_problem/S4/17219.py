import sys
input = sys.stdin.readline

n,m= map(int,input().split())

my_dict = dict()

for _ in range(n):
    address,password = input().split()
    my_dict[address] = password

for _ in range(m):
    find_pass = input().strip()
    print(my_dict[find_pass])