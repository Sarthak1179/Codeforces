n = int(input())
x = list(map(int, input().split()))
x[0] = 0
y = list(map(int, input().split()))
y[0] = 0
c = x+y
c = set(c)
if 0 in c:
    if len(c)-1 == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
else:
    if len(c) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")