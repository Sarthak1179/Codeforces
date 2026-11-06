t = int(input())
for _ in range(t):
    n = int(input())
    if n%2 != 0:
        count = n//2
    else:
        count = (n//2) - 1
    print(count)