# t = int(input())
# for i in range(t):
#     n, k = map(int, input().split())
#     a = input()
#     sp = 0
#     ep = k
#     count = 0
#     # cons = 0
#     ans = n
#     ext = 0
    
#     # while True:
#     #     for j in range(sp,ep):
#     #         if a[j] == "W":
#     #             count += 1
#     #             # print(count)
#     #     if ans > count:
#     #         ans = count
#     #     if ans == 0:
#     #         # print(0)
#     #         ext = 1
#     #         break
#     #     if ep == len(a):
#     #         break
#     #     count = 0
#     #     sp += 1
#     #     ep += 1
#     for i in range(n-k+1):
#         count = a[sp:ep].count("W")
#         if ans > count:
#             ans = count
#         sp += 1
#         ep += 1
        
#     # if ext == 0:
#     print(ans)
#     # elif ext == 1:
#     #     print(0)
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    w = s[:k].count("W")
    ans = w

    for i in range(k, n):
        if s[i] == "W":
            w += 1

        if s[i-k] == "W":
            w -= 1

        ans = min(ans, w)

    print(ans)