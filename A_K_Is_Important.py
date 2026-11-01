t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    score = 0
    while len(a)>=k:
        if a[k-1] >= a[len(a) - k]:
            score += a[k-1]
            a.pop(k-1)
        else:
            score += a[len(a) - k]
            a.pop(len(a) - k)
    print(score)
        