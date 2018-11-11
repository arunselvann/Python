for _ in range(int(input())):
    s = input()
    l = len(s)
    m = 1
    start = 0
    for i in range(1,l):
        low = i - 1
        high = i
        while low >= 0 and high < l and s[low] == s[high]:
            if high - low + 1 > m:
                start = low
                m = high - low + 1
            low -= 1
            high += 1
        low = i-1
        high = i+1
        while low >=0 and high < l and s[low] == s[high]:
            if high - low + 1 > m:
                start = low
                m = high - low + 1
            low -= 1
            high += 1
    print(s[start:start+m])
