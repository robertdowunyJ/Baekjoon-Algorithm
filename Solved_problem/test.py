r=0
s = input("Type of Mineral = ").strip()
num = int(input("Number of Mineral = "))
match s:
    case "diamond":
        r=150*4*num
    case "ruby":
        r=30*4*num
    case "coral":
        r=10*4*num
    case _:
        r = 0


print("savings =", r)

