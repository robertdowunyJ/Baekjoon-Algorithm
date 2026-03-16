n1 = input()
n2 = input()
n3 = input()

#연속으로 세개가 다 문자가 나올수없음.
#n1,n2,n3 중 숫자인거 판단해서
if n1 != "Fizz" and n1 != "Buzz" and n1 != "FizzBuzz":
    n1 = int(n1)
    k = n1+3
if n2 != "Fizz" and n2 != "Buzz" and n2 != "FizzBuzz":
    n2 = int(n2)
    k = n2 +2
if n3 != "Fizz" and n3 != "Buzz" and n3 != "FizzBuzz":
    n3 = int(n3)
    k = n3 +1

if k % 15 == 0:
    print("FizzBuzz")
elif k % 3 ==0 and k% 5 != 0:
    print("Fizz")
elif k% 3 != 0 and k % 5 == 0:
    print("Buzz")
else:
    print(k)




