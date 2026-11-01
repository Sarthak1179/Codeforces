n = int(input())
num = list(map(int, input().split()))
maxi = 1
count = 1
for i in range(1,n):
    if num[i] < num[i-1]:
        count = 1
    else:
        count += 1
        maxi = max(maxi,count)
print(maxi)