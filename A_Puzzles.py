n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
difference = a[m-1] - a[0]
for i in range(0,m-n+1):
    mini = a[i]
    maxi = a[i+n-1]
    # for j in range(i,i+n):
    #     if a[j] > maxi:
    #         maxi = a[j]
    #     if a[j] < mini:
    #         mini = a[j]
    diff = maxi - mini
    if difference > diff:
        difference = diff
print(difference)