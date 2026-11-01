n, a, b, c = map(int, input().split())
x = min(a,min(b,c))
z = max(a,max(b,c))
y = (a+b+c)-x-z
if n%x == 0:
    print(n//x)
