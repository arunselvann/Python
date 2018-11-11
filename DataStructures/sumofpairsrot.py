class sumofpairsrot():
    def findpair(self, arr, s, x):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                break;

        l = (i+1)%n
        r = i

        while (l!=r):
            print(l,r,arr[l] + arr[r],x)
            if (arr[l] + arr[r] == x):
                return True
            elif (arr[l] + arr[r] < x):
                l = (l+1) % n;
            else:
                r = (n+r-1) % n;

        return False;

sop = sumofpairsrot()
arr = [11, 15, 26, 38, 9, 10]
sum = 26
n = len(arr)

if(sop.findpair(arr, n, sum)):
    print("Found")
else:
    print("Not Found")