n, k = map(int, input().split())
a = list(map(int, input().split()))
b = n%k

for i in range(0,n,3):
    if i == n:
        break
    mini = a[i]
    if i == n-b:
        for j in range(1,b):
            # print(j)
            # print(i+b)
            # print(mini)
            if mini > a[i+j]:
                mini = a[i+j]
    else:
        for j in range(1,k):
            print(i+j)
            # print(mini)
            if mini > a[i+j]:
                mini = a[i+j]
    print(mini,end=" ")