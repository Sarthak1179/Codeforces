n, q = map(int, input().split())
for i in range(n):
    a = list(map(int, input().split()))
    a.reverse()
    print(*a)