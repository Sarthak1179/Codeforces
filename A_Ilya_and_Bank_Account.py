n = int(input())
if n>0:
    print(n)
else:
    mod10 = abs(n)%10
    last_second = (((abs(n)//100)*10) + mod10) * (-1)
    # print(last_second)
    print(max(last_second, (abs(n)//10) * (-1)))