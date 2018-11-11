class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


def findMid(head):
    if not head:
        return -1
    else:
        l = 1
        i = 0
        cur_node = head
        while cur_node.next:
            cur_node = cur_node.next
            l += 1
        cur_node = head
        while cur_node.next and i < l // 2:
            cur_node = cur_node.next
            i += 1
        return cur_node

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)
