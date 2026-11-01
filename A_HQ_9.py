x = input()
a = ['H','Q','9']
ans = False
for i in range(len(x)):
    if x[i] in a:
        ans = True
if ans:
    print("YES")
else:
    print("NO")