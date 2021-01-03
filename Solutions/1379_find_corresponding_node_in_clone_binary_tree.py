# 1379_find_corresponding_node_in_clone_binary_tree
# Keys: #tree #preorder

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        # preorder traversal to find the node in the original tree
        # use a pointer to follow the original tree
        stack = [(original, cloned)]

        while stack:
            (node, clone) = stack.pop()
            if node == target:
                return clone
            if node:
                stack.append((node.right, clone.right))
                stack.append((node.left, clone.left))
