# 0104_maximum_depth_of_binary_tree.py
# Easy
# Keys: #tree #recursion #DFS #postorder


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def checkdp(root):
            if root == None:
                return 0
            l = checkdp(root.left)
            r = checkdp(root.right)

            return 1 + max(l, r)

        return checkdp(root)

    def maxDepth1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # iterative with postorder traverse
    def maxDepth2(self, root: TreeNode) -> int:
        stack, depths = [(root, False)], {}
        if not root:
            return 0

        while stack:
            curr, visited = stack.pop()
            if visited:  # visited
                depths[curr] = 1 + max(
                    depths.get(curr.left, 0), depths.get(curr.right, 0)
                )
            else:  # not visited
                if curr:
                    stack.append((curr, True))
                    stack.append((curr.left, False))
                    stack.append((curr.right, False))

        return depths[root]
