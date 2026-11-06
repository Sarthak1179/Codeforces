a = input()
i = 0
wub = True
while i < len(a):
    if i <= len(a)-3 and a[i]+a[i+1]+a[i+2] == "WUB":
        if i > 0 and wub:
            print(" ",end="")
            wub = False
        i += 3
    else:
        print(a[i],end="")
        i += 1
        wub = True