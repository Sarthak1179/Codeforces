n = int(input())
nums = list(map(int, input().split()))
even_count = 0
odd_count = 0
even = 0
odd = 0
for i in range(n):
    if nums[i]%2 == 0:
        even_count += 1
        even = i+1
    else:
        odd_count += 1
        odd = i+1
if even_count>odd_count:
    print(odd)
else:
    print(even)