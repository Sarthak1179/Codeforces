n = int(input())
coins = list(map(int, input().split()))
coins.sort()
coins.reverse()
d1 = 0
d2 = sum(coins)
count = 0
i = 0
while d2 >= d1:
    d1 += coins[i]
    d2 -= coins[i]
    count += 1
    i += 1
print(count)