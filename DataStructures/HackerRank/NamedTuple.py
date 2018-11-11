from collections import namedtuple
N = int(input())
Total = 0
Fields = list(input().strip().split())
Marks = namedtuple('Marks',Fields)
for i in range(N):
    Field1, Field2, Field3, Field4 = input().strip().split()
    M1 = Marks(Field1, Field2, Field3, Field4)
    Total += int(M1.MARKS)
print(Total/N)