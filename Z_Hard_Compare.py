import math
a, b, c, d = map(int,input().split())
if (b*math.log10(a)) > (d*math.log10(c)):
    print("YES")
else:
    print("NO")