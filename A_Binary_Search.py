n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

for i in range(k):
    flag = 0
    s = 0
    e = n-1
    while s <= e:
        mid = (s+e)//2
        if a[mid] == q[i]:
            flag = 1
            break
        if a[mid] > q[i]:
            e = mid - 1
        else:
            s = mid + 1
    if flag == 1:
        print("YES")
    else:
        print("NO")