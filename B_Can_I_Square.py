t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += a[i]
    # print(ans**(1/2))
    x = ans**(1/2)
    if x%int(x) == 0:
        print("YES")
    else:
        print("NO")