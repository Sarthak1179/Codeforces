n = int(input())
first = 0
count = 0
for i in range(n):
    a = int(input())
    if i == 0:
        first = a
        count += 1
    if a == first:
        pass
    else:
        first = a
        count += 1
print(count)