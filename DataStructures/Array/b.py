if __name__ == '__main__':
    a = []
    r = [False]*5
    k = 0
    s = input()
    for i in s:
        a.append(i.isalnum())
        a.append(i.isalpha())
        a.append(i.isdigit())
        a.append(i.islower())
        a.append(i.isupper())

    for i in a:
        if k > 4:
            k = 0
        if i:
            r[k] = i
            k += 1
    for i in r:
        print(i)