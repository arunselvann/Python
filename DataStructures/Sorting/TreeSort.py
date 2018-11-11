class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeSort:
    def __init__(self, data):
        root_node = Node(data)
        self.root = root_node

    def insert(self, data):
        new_node = Node(data)
        self._insert(self.root, new_node)

    def _insert(self, root, node):
        if root.data >= node.data:
            if root.left:
                self._insert(root.left,node)
            else:
                root.left = node
        else:
            if root.right:
                self._insert(root.right, node)
            else:
                root.right = node

    def sort(self, root):
        if root:
            self.sort(root.right)
            print(root.data, end=' ')
            self.sort(root.left)


s = TreeSort(2)
for i in range(10,-1,-1):
    s.insert(i)
s.sort(s.root)