def lastIndex(s):
    if s is not None:
        l = len(s)-1
        for i in range(l,-1,-1):
            if s[i] == '1':
                return i
    return -1

for _ in range(int(input())):
    print(lastIndex(input()))

