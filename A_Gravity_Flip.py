t = int(input())
a = list(map(int, input().split()))
length = len(a)
col = [0]*t
for i in range(max(a)):
    count = 0
    for j in range(length):
        if a[j] >= 1:
            count += 1
            a[j] -= 1
    for j in range(length-count,length):
        col[j] += 1
print(*col)