class Queue:
    def __init__(self):
        self.q = []

    def is_queue_empty(self):
        return len(self.q) == 0

    def enQueue(self, data):
        self.q.insert(0, data)

    def deQueue(self):
        if self.is_queue_empty():
            print("Queue is empty")
        else:
            return self.q.pop()

    def peak(self):
        if not self.is_queue_empty():
            return self.q[-1].data

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.q)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def level_order(self, start):
        if not start:
            return
        Q = Queue()
        Q.enQueue(start)
        traversal = ""

        while len(Q) > 0:
            traversal += str(Q.peak()) + "-"
            node = Q.deQueue()

            if node.left:
                Q.enQueue(node.left)
            if node.right:
                Q.enQueue(node.right)

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.level_order(tree.root))