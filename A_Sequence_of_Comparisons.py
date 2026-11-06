t = int(input())
for _ in range(t):
    sign = input()
    if '<' not in sign:
        if '>' in sign:
            print(">")
        else:
            print("=")
    elif '>' not in sign:
        if '<' in sign:
            print("<")
        else:
            print("=")
    else:
        print("?")