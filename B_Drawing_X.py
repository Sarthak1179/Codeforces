
n = int(input())

for i in range(n):
    row = ["*"] * n

    if i < n // 2:
        row[i] = "\\"
        row[n - 1 - i] = "/"
    elif i > n // 2:
        row[n - 1 - i] = "/"
        row[i] = "\\"
    else:
        row[i] = "X"

    print("".join(row))