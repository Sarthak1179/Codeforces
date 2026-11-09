t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    mini_total = (k*(k+1)) / 2
    maxi_total = ((2*n-k+1)*k) / 2
    if x >= mini_total and x <= maxi_total:
        print("YES")
    else:
        print("NO")