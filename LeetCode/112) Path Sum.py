from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root: Optional[TreeNode]):
    if root:
        print(root.val, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def in_order_traversal(root: Optional[TreeNode]):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=' ')
        in_order_traversal(root.right)


def post_order_traversal(root: Optional[TreeNode]):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=' ')


def level_order_traversal(root: Optional[TreeNode]):
    if not root:
        return

    queue = [root]

    while len(queue) > 0:
        cur_node = queue.pop(0)
        print(cur_node.val, end=' ')

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(cur_node, cur_sum):
            if not cur_node:
                return False

            cur_sum += cur_node.val
            if not cur_node.left and not cur_node.right:
                return cur_sum == targetSum

            return dfs(cur_node.left, cur_sum) or dfs(cur_node.right, cur_sum)

        return dfs(root, 0)


tree = TreeNode(5)
tree.left = TreeNode(4)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right = TreeNode(8)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.right = TreeNode(1)

pre_order_traversal(tree)
print()
in_order_traversal(tree)
print()
post_order_traversal(tree)
print()
level_order_traversal(tree)
