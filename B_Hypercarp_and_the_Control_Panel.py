t = int(input())
for i in range(t):
    l = int(input())
    a = list(map(int, input().split()))
    count = 0
    swap = 1
    for i in range(l-1):
        if swap == 1 and i < l-2 and (a[i] == a[i+1]) and (a[i+2] != a[i]):
                x = a[i+1]
                y = a[i+2]
                a[i+1] = y
                a[i+2] = x
                swap = 0
        elif a[i] == a[i+1]:
            count += 1
    print(l-count)