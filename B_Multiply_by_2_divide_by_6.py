t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    isava = True
    while n>1:
        if n==2 or n==4 or n==5 or n%3 != 0:
            isava = False
            break
        else:
            if n%6 == 0:
                count += 1
                n //= 6
            else:
                count += 1
                n *= 2
    if isava:
        print(count)
    else:
        print("-1")
# This problem can have more eliable solution with better time complaxity