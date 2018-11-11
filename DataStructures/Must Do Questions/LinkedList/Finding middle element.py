class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, length):
        self.head = None
        self.length = length

    def isListEmpty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)
        if self.isListEmpty():
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node

    def printList(self):
        if self.isListEmpty():
            return -1
        else:
            i = 0
            cur_node = self.head
            while cur_node.next and i < self.length//2:
                cur_node = cur_node.next
                i += 1
            return cur_node.data


T = int(input())
r = []
for i in range(T):
    N = int(input())
    l = LinkedList(N)
    arr = list(input().split())
    for i in arr:
        l.insert(i)
    r.append(l.printList())
for i in r:
    print(i)

