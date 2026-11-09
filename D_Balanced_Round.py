t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    # zero = a.count(0)
    # del a[0:zero]
    count = 1
    final_count = 0
    for i in range(n - 1):
        if abs(a[i] - a[i+1]) <= k:
            count += 1
        else:
            # if count > final_count:
            #     final_count = count
            count = 1
        if count > final_count:
            final_count = count
    if count > final_count:
        final_count = count
    print(n - final_count)