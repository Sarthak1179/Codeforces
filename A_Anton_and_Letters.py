s = set(input().strip("{}").replace(" ", "").split(","))
# s = list(s)
if '' in s:
    print(0)
else:
    print(len(s))