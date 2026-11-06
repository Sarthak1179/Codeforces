t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    char = {}
    for i in range(n):
        if s[i] in char:
            if char[s[i]] == 1:
                char[s[i]] = 0
            else:
                char[s[i]] += 1
        else:
            char[s[i]] = 1
    if sum(char.values()) - k > 1:
        print("NO")
    else:
        print("YES")