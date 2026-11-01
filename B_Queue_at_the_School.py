n,t = map(int, input().split())
x = list(input())
for i in range(t):
    j = 0
    while j < n-1:

        if x[j] == "B" and x[j+1] == "G":
            x[j], x[j+1] = x[j+1], x[j]
            j += 2
        else:
            j += 1
for i in x:
    print(i,end="")