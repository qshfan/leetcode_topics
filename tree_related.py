# Problems orgnized according to link:
# https://github.com/liyin2015/Algorithms-and-Coding-Interviews/blob/master/tree_questions.pdf

# Tree problems categories:
# - Binary Tree
#   - tree traversal
#   - tree property (Depth, height, diameter)
#   - tree advanced property, LCA
#   - tree path
#   - Hoc

# - BST
#   - BST rules
#   - operations
#   - find certain element of the tree
#   - trim tree
#   - split tree


# Problem list:

# Tree Traversal (easier using recursive)
# LC. 144 Binary tree preorder traversal
# LC. 145 Binary Tree Postorder Traversal
# LC. 94 Binary Tree Inorder Traversal
# LC. 103 Binary Tree Zigzag Level Order Traversal
# LC. 105 Construct Binary Tree from Preorder and Inorder Traversal
# LC. 429 N-ary Tree Level Order Traversal
# LC. 590 N-ary Tree Postorder Traversal

# Tree Property


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


# 2-2 th way: iterative  once in and out from stack, add checks of node.right
def postorderTraversal_6(root):
    stack, node, last = [], root, None
    res = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                res.append(node.val)
                last = node
                node = None
            else:
                node = node.right
    return res


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
    # Note: parents is a queue, not a stack
    parents, res = [root], []
    direction = 1
    while root and parents:
        child = []
        if direction:
            res.append([parent.val for parent in parents])
        else:
            res.append([parent.val for parent in reversed(parents)])
        direction ^= 1
        for parent in parents:
            if parent.left:
                child.append(parent.left)
            if parent.right:
                child.append(parent.right)
        parents = child
    return res


# another way of using direction (avoiding code repeating):
def zigzagLevelOrder_1(root):
    if not root:
        return None
    queue = [root]
    flag = 1
    res = []
    while queue:
        res.append([node.val for node in queue[::flag]])
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        flag *= -1
    return res


# LC. 105 Construct Binary Tree from Preorder and Inorder Traversal
# did end up solving it
# def buildTree(preorder, inorder):
#     lut = {}
#     for index, elem in enumerate(inorder):
#         lut[elem] = index
#     pt, stack = 0, []

#     while pt < len(preorder) - 1:
#         node = TreeNode(preorder[pt])
#         stack += [node]
#         if (
#             lut[preorder[pt + 1]] < lut[preorder[pt]]
#         ):  # next node at left side (direct child)
#             node.left = TreeNode(preorder[pt + 1])
#         else:  # next node at right side, not necessary direct child
#             # moving right, probably hit a leaf. -- pop it out from stack
#             left_leaf = stack.pop()
#         pt += 1


def buildTree(preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree(preorder, inorder[0:ind])
        root.right = buildTree(preorder, inorder[ind + 1 :])
        return root


# optimized with map
def buildTree_2(preorder, inorder):
    inor_dict = {}
    for i, num in enumerate(inorder):
        inor_dict[num] = i
    pre_iter = iter(preorder)

    def helper(start, end):
        if start > end:
            return None
        root_val = next(pre_iter)
        root = TreeNode(root_val)
        idx = inor_dict[root_val]
        root.left = helper(start, idx - 1)
        root.right = helper(idx + 1, end)
        return root

    return helper(0, len(inorder) - 1)


# Iterative solution
# https://leetcode.wang/leetcode-105-Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.html#解法二-迭代-栈
def buildTree_3(preorder, inorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    stack = []
    stack.append(root)

    pre = 1
    ino = 0
    while pre < len(preorder):
        curr = TreeNode(preorder[pre])
        pre += 1
        prev = None

        # come from root, go through list preorder
        # do two things: append current node to left or to right
        # use stack to manipulate location where you want tree to keep growing.
        # make the whole tree concatenate.

        while stack and stack[-1].val == inorder[ino]:
            prev = stack.pop()
            ino += 1
        if prev:
            prev.right = curr
        else:
            stack[-1].left = curr

        stack.append(curr)
    return root


# LC. 429 N-ary Tree Level Order Traversal
def levelOrder(root):
    queue = [root]
    res = []
    while queue and root:
        tmp, children = [], []
        for e in queue:
            if e:
                tmp += e.children
                children.append(e.val)
        res.append(children)
        queue = tmp

    return res


# solution with deque -- slower and dont need deque....
import collections


def levelOrder_2(root):
    if not root:
        return []

    traversal = []
    queue = collections.deque()
    queue.append((root, 0))

    while queue:
        node, level = queue.popleft()

        if node:
            traversal_depth = len(traversal) - 1
            if traversal_depth < level:
                traversal.append([])

            traversal[level].append(node.val)

            for child in node.children:
                queue.append((child, level + 1))

    return traversal


# LC. 590 N-ary Tree Postorder Traversal
# recursive
def postorder(root):
    res = []
    dfs2(root, res)
    return res


def dfs2(root, res):
    if root:
        for c in root.children:
            dfs2(c, res)
        res.append(root.val)


# recursive self
def postorder_1(root):
    if not root:
        return []
    if not res:
        res = []
    for i in root.children:
        res += postorder_1(i)
    return res + [root.val]


# recursive using yield
def postorder_3(root):
    return list(traverse_in_postorder(root))


def traverse_in_postorder(tree):
    if tree:
        for child in tree.children:
            yield from traverse_in_postorder(child)
        yield tree.val


# iterative -- changed from preorder traversal
def postorder_2(root):
    res = []
    if not root:
        return None
    stack = [root]
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        stack.extend(curr.children)
    return res[::-1]


#########################################################
#      Tree Properties (Depth, Height, Diameter)        #
#########################################################

# LC. 111 Minimum Depth of Binary Tree
def minDepth(root):
    l, i = [root], 1
    while l and root and all(n.left or n.right for n in l):
        l, i = [kid for n in l for kid in [n.left, n.right] if kid], i + 1
    return i if root else 0


# LC. 110 Balanced Binary Tree
# recursive
def check(node):
    if node == None:
        return (0, True)
    l_depth, l_balanced = check(node.left)
    r_depth, r_balanced = check(node.right)
    return (
        max(l_depth, r_depth) + 1,
        l_balanced and r_balanced and abs(l_depth - r_depth) <= 1,
    )


def isBalanced(root):
    return check(root)[1]


# iterative , based on postorder traversal
def isBalanced_1(root):
    stack, node, last, depths = [], root, None, {}
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True


# iterative  -- this is based on iterative solution from postorder.
def isBalanced_2(root):
    stack = [(root, False)]
    depths = {}

    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                depth_left, depth_right = 0, 0
                if node.left:
                    depth_left = depths[node.left]
                if node.right:
                    depth_right = depths[node.right]
                if abs(depth_right - depth_left) > 1:
                    return False
                depths[node] = max(depth_right, depth_left) + 1
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

    return True


# LC. 543
# LC. 559
# LC. 104
#

#########################################################
#            Tree advanced property, LCA                #
#########################################################
