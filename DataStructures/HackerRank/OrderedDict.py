from collections import OrderedDict

od, N = OrderedDict(), int(input())
for _ in range(N):
    Items = list(input().strip().split())
    Item = ''
    Price = 0
    for i, j in enumerate(Items):
        if i < len(Items)-1:
            Item += j + ' '
        else:
            Price = int(j)
    try:
        od[Item.strip()] += Price
    except KeyError:
        od[Item.strip()] = Price

for i in od:
    print(i,od[i])