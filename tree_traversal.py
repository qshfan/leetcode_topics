# Problems orgnized according to link:
# https://github.com/liyin2015/Algorithms-and-Coding-Interviews/blob/master/tree_questions.pdf

# Tree problems categories:
# - Binary Tree
#   - tree traversal
#   - tree property
#   - tree advanced property, LCA
#   - tree path
#   - Hoc

# - BST
#   - BST rules
#   - operations
#   - find certain element of the tree
#   - trim tree
#   - split tree

# Get to know tree - Implementation
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


root = TreeNode(12)
# TODO: How to insert null Nodes?
tail = [3, 2, 4, 9, 8, 15, 20, 3, 14, 22, 100, 30, 40, 51, 21, 25, 66]
for elem in tail:
    root.insert(elem)


print("Original Tree: ")
print(root.PrintTree())


# LC. 144 Binary tree preorder traversal
# def preorderTraversal(root):
#     res = []
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         print("-----------> get new node from stack")
#         if node:
#             print("Deal with: ", node.val)
#             res.append(node.val)
#             stack.append(node.right)
#             # visualize stack
#             if node.right:
#                 print(f"add {node.right.val} to right stack")
#             else:
#                 print("add none to right")
#             stack.append(node.left)
#             if node.left:
#                 print(f"add {node.left.val} to left stack")
#             else:
#                 print("add none to left")
#     return res
def preorderTraversal(root):
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res


# print(preorderTraversal(root))

# LC. 145 Binary Tree Postorder Traversal
# Idea is very similar with preorder, just need to push twice.
def postorderTraversal(root):
    res = []
    if not root:
        return res
    stack = [root] * 2
    while stack:
        node = stack.pop()
        if stack and stack[-1] is node:
            if node.right:
                stack += [node.right] * 2
            if node.left:
                stack += [node.left] * 2
        else:
            res.append(node.val)
    return res


# 2nd way, can add one dimension on stack, store if a node is visited
def postorderTraversal_2(root):
    traversal, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                # add to result if visited
                traversal.append(node.val)
            else:
                # post-order
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

    return traversal


# 3rd way: do preorder, then reverse the result -- also reverse the order to append to stack (first left then right)
def postorderTraversal_3(self, root):
    traversal, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            # pre-order, right first
            traversal.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

    # reverse result
    return traversal[::-1]


# 4th way: recursively
def postorderTraversal_4(self, root):
    res = []
    self.dfs(root, res)
    return res


def dfs(self, root, res):
    if root:
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)


# 5th way: different form of recursive
def postorderTraversal_5(root):
    if root:
        return (
            postorderTraversal_5(root.left)
            + postorderTraversal_5(root.right)
            + [root.val]
        )
    else:
        return []


# LC. 94 Binary Tree Inorder Traversal
# use 5th solution from postorder:
def inorderTraversal(root):
    if root:
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    else:
        return []


# iterative
def inorderTraversal_2(root):
    res, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            res.append(tmpNode.val)
            root = tmpNode.right
    return res


# LC. 103 Binary Tree Zigzag Level Order Traversal
# append node.val, not append node..
def zigzagLevelOrder(root):
    parents, res = [root], []
    while parents:
        child = []
        res.append([parents])
        for parent in parents:
            if parent:
                child.append(parent.left, parent.right)
        parents = child
    return res
