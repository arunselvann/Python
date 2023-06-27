# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def pre_order(node):
            if not node:
                result.append('n')
                return

            result.append(str(node.val))
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)
        print(result)
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split()

        def pre_order():
            item = data.pop(0)
            if item == 'n':
                return None
            root = TreeNode(item)
            root.left = pre_order()
            root.right = pre_order()
            return root

        return pre_order()


# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(ser.serialize(ans))
