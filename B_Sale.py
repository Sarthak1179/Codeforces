n, m = map(int, input().split())
price = list(map(int, input().split()))
price.sort()
wallet = 0
for i in range(m):
    if price[i] < 0:
        wallet += abs(price[i])
    else:
        break
print(wallet)