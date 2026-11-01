n = int(input())
a = list(map(int, input().split()))
sp = 0
ep = n-1
s = 0
d = 0
while sp-1 != ep:
    if a[sp] > a[ep]:
        s += a[sp]
        sp += 1
    else:
        s += a[ep]
        ep -= 1
    if sp-1 == ep:
        break
    if a[sp] > a[ep]:
        d += a[sp]
        sp += 1
    else:
        d += a[ep]
        ep -= 1
print(s, d)