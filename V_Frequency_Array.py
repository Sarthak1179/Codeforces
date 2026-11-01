n, q = map(int, input().split())
a = list(map(int, input().split()))
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
for i in range(1,q+1):
    if i in b:
        print(b[i])
    else:
        print(0)