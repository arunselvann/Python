def pc(arr):
    s = []
    for i in arr:
        if i == '{' or i =='(' or i == '[':
            s.append(i)
        elif (i == '}' or i ==')' or i == ']') and len(s) != 0:
            if (i == '}' and s[-1] == '{') or (i ==')' and s[-1] == '(') or (i == ']' and s[-1] == '['):
                s.pop()
            else:
                return 1
        else:
            return 1
    return len(s)

N = int(input())
r = []
for i in range(N):
    r.append(pc(list(input())))
for i in r:
    if i == 0:
        print('balanced')
    else:
        print('not balanced')




