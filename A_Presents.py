n = int(input())
lis = list(map(int, input().split()))
ans = [0]*max(lis)
for i in range(n):
    ind = lis[i] - 1 
    ans[ind] = i+1
print(*ans)