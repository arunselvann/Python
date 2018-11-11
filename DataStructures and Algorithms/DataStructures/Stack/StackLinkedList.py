class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class StackLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def islistempty(self):
        if self.head:
            return False
        else:
            return True

    def push(self, data):
        new_node = Node(data)
        if self.islistempty():
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.tail = new_node
        self.length += 1
        print("pushed", new_node.data)

    def pop(self):
        if self.islistempty():
            print('List is empty')
        elif self.head.next is None:
            print("Popped", self.head.data)
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            cur_node = self.head
            while cur_node.next:
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = None
            self.tail = prev_node
            print("Popped", cur_node.data)
            del cur_node
            self.length -= 1

    def top(self):
        if self.islistempty():
            print('List is empty')
        else:
            print("The top is", self.tail.data)

    def size(self):
        print(self.length)

    def print(self):
        if self.islistempty():
            print('List is empty')
        else:
            cur_node = self.head
            while cur_node.next:
                print(cur_node.data, end=" ")
                cur_node = cur_node.next
            print(cur_node.data)


s = StackLinkedList()
s.size()
s.print()
s.top()
s.push(1)
s.size()
s.top()
s.push(2)
s.top()
s.push(3)
s.push(4)
s.top()
s.print()
s.pop()
s.print()
s.size()
s.pop()
s.top()
s.size()
s.pop()
s.top()
s.size()
s.pop()
s.top()
s.size()
s.print()
s.pop()
s.size()
s.top()