# 0297_serialize_binary_tree
# Keys:
# BFS, deque, str ops (split, join), rebuild tree

# Code Quality Hacks:
# Use deque, pop the elements, instead of for loop, swaping array.
# seperator in the loop: avoid to many of them (e.g. return ','.join(res) for line seperation)
# avoiding to much index munipulation
# Understan the problem better, subarray of each level of tree is not needed

# Complexity: Time O(n), Space O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Codec:
    def serialize(self, root):
        if not root:
            return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else "#")
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        index = 1
        while q:
            node = q.popleft()
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


##################
# my code:
##################
class Codec_mycode:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # BFS, traversal the tree, keep all nodes
        # -- drawback: when tree not balanced, additional space complexity
        res, queue, children = "", [root], []

        while queue:
            # turn the tree to string
            for node in queue:
                if node:  # if not None, add children to queue
                    children.append(node.left)
                    children.append(node.right)
                    res += "," + str(node.val)
                else:
                    # else, node is None, no need to record it's children
                    res += "," + " "
            res += ";"
            # move deeper
            queue = children
            children = []
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_arr = data[:-1].split(";")
        # get root:
        root_val = tree_arr[0][1:].split(",")
        root = None if root_val[0] == " " else TreeNode(int(root_val[0]))

        queue = [root]
        next_queue = []
        for _, nodes in enumerate(tree_arr[1:]):
            cnt = 0
            node_arr = nodes[1:].split(",")
            for node in queue:
                if node:
                    node.left = (
                        None if node_arr[cnt] == " " else TreeNode(int(node_arr[cnt]))
                    )
                    node.right = (
                        None
                        if node_arr[cnt + 1] == " "
                        else TreeNode(int(node_arr[cnt + 1]))
                    )
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                    cnt += 2
            queue = next_queue
            next_queue = []

        return root