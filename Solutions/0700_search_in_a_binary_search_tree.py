# 0700_search_in_a_binary_search_tree.py
# Easy
# Keys: #BST #recursion #DFS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if root == None or root.val == val:
            return root

        while root != None and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right

        return root

    def searchBST_recursive(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)