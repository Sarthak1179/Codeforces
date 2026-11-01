# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# q = list(map(int, input().split()))

# for i in range(k):
#     e = n-1
#     while q[i] >= a[e]:
#         e = e/2
    
#     print(e)
n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

for x in q:
    left = 0
    right = n - 1
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if a[mid] <= x:
            ans = mid + 1
            left = mid + 1
        else:
            right = mid - 1

    print(ans)