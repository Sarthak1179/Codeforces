n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [0]
ans = 0
for i in range(n):
    if i == 0:
        x.append(a[i])
    else:
        x.append(x[i] + a[i])
for i in range(q):
    b = list(map(int, input().split()))
    ans += x[b[1]] - x[b[0]-1]
    print(ans)
    ans = 0