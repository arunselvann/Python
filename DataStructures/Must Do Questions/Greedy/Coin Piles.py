def cp(n, k, arr):
    r = sum(arr)
    for i in range(n):
        for j in range(i+1, n):
            if abs(arr[i]-arr[j]) > k:
                r += abs(arr[i]-arr[j]) - k
                if arr[i] >= arr[j]:
                    arr[i] -= abs(arr[i]-arr[j]) - k
                else:
                    arr[j] -= abs(arr[i]-arr[j]) - k
    print(r-sum(arr))


for _ in range(int(input())):
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    cp(n, k, arr)


1
42 468
335 501 170 725 479 359 963 465 706 146 282 828 962 492 996 943 828 437 392 605 903 154 293 383 422 717 719 896 448 727 772 539 870 913 668 300 36 895 704 812 323 334