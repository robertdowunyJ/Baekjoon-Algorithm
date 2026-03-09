max_num = 0
max_idx = 0

lst =[]
for i in range(9):
    n = int(input())
    lst.append(n)

for i in range(9):
    if lst[i] > max_num:
        max_num = lst[i]
        max_idx = i

print(max_num)
print(max_idx+1)