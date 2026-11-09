t = int(input())
for _ in range(t):
    n = int(input())
    mod = n%2020
    floor =  n//2020
    if (2021*floor) >= n:
        print("YES")
    else:
        print("NO")