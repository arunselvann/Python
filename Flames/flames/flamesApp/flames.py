def flames(str1, str2):
    d = {'f': 'You both are friends',
         'l': 'You love each other',
         'a': 'You guys have affection',
         'm': 'You guys are gonna get married',
         'e': 'You hate each other',
         's': 'You guys are siblings'}
    r1 = [0] * 26
    r2 = [0] * 26
    for j in list(str1.upper()):
        k = ord(j) - 65
        r1[k] += 1
    for j in list(str2.upper()):
        k = ord(j) - 65
        r2[k] += 1
    for i in range(26):
        r1[i] = abs(r1[i] - r2[i])
    n = sum(r1)
    arr = ['f', 'l', 'a', 'm', 'e', 's']
    ptr = -1
    l = 6
    for i in range(5):
        j = n % l
        if j == 0:
            j = n
        while j > 0:
            ptr += 1
            if ptr > l - 1:
                ptr = 0
            j -= 1
        arr.pop(ptr)
        ptr -= 1
        l -= 1
    return d[arr[0]]
