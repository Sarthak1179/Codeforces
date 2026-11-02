n, m = map(int, input().split())
tasks = list(map(int, input().split()))

current = 1
total = 0

for i in range(m):
    if tasks[i] >= current:
        total += tasks[i] - current
    else:
        total += (n - current) + tasks[i]

    current = tasks[i]

print(total)