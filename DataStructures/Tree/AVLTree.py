class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root:
            self._insert(self.root, new_node)
        else:
            self.root = new_node

    def __repr__(self):
        if self.root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.data != None:
                    buf = ' ' * int((5 - len(str(n.data))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.data), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left != None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right != None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def _insert(self, root, node):
        if node.data < root.data:
            if root.left:
                self._insert(root.left, node)
            else:
                root.left = node
                root.left.parent = root
                self._inspect_insertion(root.left)
        elif node.data > root.data:
            if root.right:
                self._insert(root.right, node)
            else:
                root.right = node
                root.right.parent = root
                self._inspect_insertion(root.right)
        else:
            print("Value is already in the tree")

    def print_tree(self):
        if self.root:
            return self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(node.data, node.heigh)
            self._print_tree(node.right)

    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node.parent is None:
            return
        path = [cur_node] + path

        left_height = self.get_height(cur_node.parent.left)
        right_height = self.get_height(cur_node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1+cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.rigth and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')

    def get_height(self, cur_node):
        if cur_node is None:
            return 0
        return cur_node.height

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3
        if t3 != None: t3.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 != None:
            t2.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))


a = AVLTree()
for i in range(10):
    print ("Inserting %d"%i)
    a.insert(i)
    print(a)