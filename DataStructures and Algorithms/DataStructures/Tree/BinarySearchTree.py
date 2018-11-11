class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, node):
        if self.data >= node.data:
            if self.left:
                return self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                return self.right.insert(node)
            else:
                self.right = node

    def print(self):
        if self:
            if self.left:
                self.left.print()
            print(self.data, end=" ")
            if self.right:
                self.right.print()


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_tree_empty(self):
        return self.root is None

    def insert(self, data):
        new_node = Node(data)

        if self.is_tree_empty():
            self.root = new_node
        else:
            return self.root.insert(new_node)

    def print(self):
        self.root.print()

t = BinarySearchTree()
t.insert(50)
t.insert(40)
t.insert(70)
t.insert(70)
t.insert(10)
t.insert(20)
t.insert(80)
t.insert(60)
t.insert(30)
t.insert(90)
t.print()