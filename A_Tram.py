n = int(input())
count_max = 0
current_ava = 0
for _ in range(n):
    a, b = map(int, input().split())
    current_ava -= a
    current_ava += b
    count_max = max(current_ava,count_max)
print(count_max)