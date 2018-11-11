class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def islistempty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert(self, data, position):
        new_node = Node(data)
        cur_node = self.head
        cur_position = 0

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            while True:
                if cur_position == position:
                    prev_node.next = new_node
                    new_node.next = cur_node
                    break
                prev_node = cur_node
                cur_node = cur_node.next
                cur_position += 1

    def append(self, data):
        new_node = Node(data)
        if self.islistempty():
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node

    def delete(self, position):
        cur_node = self.head
        cur_position = 0

        if self.islistempty():
            print("List is Empty")
        elif position == 0:
            prev_node = self.head
            self.head = self.head.next
            del prev_node
        else:
            while True:
                if cur_position == position:
                    prev_node.next = cur_node.next
                    del cur_node
                    break
                prev_node = cur_node
                cur_node = cur_node.next
                cur_position += 1

    def deletelist(self):
        if self.islistempty():
            print("List is Empty")
        else:
            del self.head

    def length(self):
        if self.islistempty():
            print("List is Empty")
        else:
            cur_node = self.head
            list_length = 1
            while cur_node.next:
                list_length += 1
                cur_node = cur_node.next
            print(list_length)

    def display(self):
        if self.islistempty():
            print("List is Empty")
        else:
            cur_node = self.head
            while cur_node.next:
                print(cur_node.data, end="")
                cur_node = cur_node.next
            print(cur_node.data)


ll = SinglyLinkedList()
ll.length()
ll.display()
ll.insert(8,0)
ll.length()
ll.append(1)
ll.append(2)
ll.append(4)
ll.display()
ll.insert(3,2)
ll.display()
ll.delete(4)
ll.display()
ll.delete(0)
ll.display()
ll.length()
ll.deletelist()
