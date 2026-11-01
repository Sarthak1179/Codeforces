t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    count = a%b
    if count == 0:
        print(0)
    else:
        print(b-count)