class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_list_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert(self, data, position=0):
        new_node = Node(data)
        cur_position = 1
        if position == 0:
            if self.is_list_empty():
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            cur_node = self.head
            while True:
                if cur_position == position:
                    if cur_node.next is None:
                        cur_node.next = new_node
                        new_node.prev = cur_node
                    else:
                        new_node.next = cur_node.next
                        cur_node.next.prev = new_node
                        cur_node.next = new_node
                        new_node.prev = cur_node
                    break
                cur_node = cur_node.next
                cur_position += 1

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if self.is_list_empty():
            self.head = new_node
        else:
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node

    def print_list(self):
        if self.is_list_empty():
            print('List is Empty')
        else:
            print('Forward Print')
            cur_node = self.head
            while cur_node.next:
                print(cur_node.data, end=" ")
                cur_node = cur_node.next
            print(cur_node.data)
            tail = cur_node

            print('Reverse Print')
            while tail.prev:
                print(tail.data, end=" ")
                tail = tail.prev
            print(tail.data)

dll = DoublyLinkedList()
dll.insert(0)
dll.append(1)
dll.append(2)
dll.insert(3)
dll.insert(4,4)
dll.print_list()

