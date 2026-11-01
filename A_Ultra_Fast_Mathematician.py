n = input()
k = int(input())
count = len(str(n))
n = int(n)
ans = []
while count>0:
    if n%10 == 0:
        if k%10 == 0:
            ans.insert(0,0)
        else:
            ans.insert(0,1)
    else:
        if k%10 == 0:
            ans.insert(0,1)
        else:
            ans.insert(0,0)
    n //= 10
    k //= 10
    count -= 1
print(*ans,sep="")