t = int(input())
for _ in range(t):
    n = int(input())
    while n%2 == 0:
        n //= 2
    if n > 1:
        print("YES")
    else:
        print("NO")
    # divi = False
    # if n%2 == 0:
    #     for i in range(3, int(n**(1/2))+1, 2):
    #         if n%i == 0:
    #             divi = True
    #             break
    # else:
    #     divi = True
    # if divi:
    #     print("YES")
    # else:
    #     print("NO")