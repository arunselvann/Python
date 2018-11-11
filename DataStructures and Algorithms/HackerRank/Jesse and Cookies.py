import heapq

def cookies(k, A):
    heapq.heapify(A)
    result = 0
    for i in range(len(A)):
        if A[0] < k and len(A)>1:
            c1 = heapq.heappop(A)
            c2 = heapq.heappop(A)
            r = (1*c1)+(2*c2)
            heapq.heappush(A, r)
            result += 1
        else:
            break
    if A[0] < k:
        print(-1)
    else:
        print(result)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    A = list(map(int, input().rstrip().split()))
    result = cookies(k, A)
