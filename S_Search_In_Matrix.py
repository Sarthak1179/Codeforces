n, q = map(int, input().split())
b = []
for i in range(n):
    b.append(i)
for i in range(n):   
    a = list(map(int, input().split()))
    b[i]=a
x = int(input())
y = 0
for i in range(n):
    for j in range(q):
        if b[i][j] == x:
            print("will not take number")
            y = 0
            break
        else:
            y = 1
if y == 1:
    print("will take number")