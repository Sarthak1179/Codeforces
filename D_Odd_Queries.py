t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)%2
    for i in range(q):
        l, r, k = map(int, input().split())
        old = sum(a[l-1:r])%2
        if (total-old+(k*(r-l+1)))%2 == 0:
            print("NO")
        else:
            print("YES")