class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularSinglyLinkedList():
    def __init__(self):
        self.head = None

    def is_list_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert(self, data, position=0):
        new_node = Node(data)
        if self.is_list_empty():
            self.head = new_node
            self.head.next = self.head
        elif position == 0:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            cur_node = self.head
            cur_position = 1
            while cur_node:
                if position == cur_position:
                    break
                cur_node = cur_node.next
                cur_position += 1
            new_node.next = cur_node.next
            cur_node.next = new_node

    def append(self, data):
        new_node = Node(data)
        if self.is_list_empty():
            self.head = new_node
            self.head.next = self.head
        else:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head

    def display(self):
        if self.is_list_empty():
            print('List is empty')
        else:
            cur_node = self.head
            while cur_node:
                print(cur_node.data, end=" ")
                cur_node = cur_node.next
                if cur_node == self.head:
                    print()
                    break


ll = CircularSinglyLinkedList()
ll.display()
ll.insert(0)
ll.display()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.display()
ll.insert(9,5)
ll.display()
