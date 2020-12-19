# Problems orgnized according to link:
# https://github.com/liyin2015/Algorithms-and-Coding-Interviews/blob/master/tree_questions.pdf

# Tree problems categories:
# - Binary Tree
#   - tree traversal
#   - tree property (Depth, height, diameter)
#   - tree advanced property, LCA
#   - tree path
#   - Reconstruct the Tree
#   - AD HOC Problems

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
# LC. 111 Minimum Depth of Binary Tree
# LC. 110 Balanced Binary Tree
# LC. 543 Diameter of Binary Tree
# LC. 559 Maximum Depth of N-ary Tree
# LC. 104 Maximum Depth of Binary Tree

# Path:
# LC. 112 Path Sum
# LC. 113 Path Sum II
# LC. 129 Sum Root to Leaf Numbers
# LC. 257 Binary Tree Paths

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


# LC. 543 Diameter of Binary Tree
# recursive
def diameterOfBinaryTree(self, root: TreeNode) -> int:
    dia = 0
    return self.depth(root, dia)[1]


def depth(self, node: TreeNode, dia: int) -> int:
    if node:
        left, dia_left = self.depth(node.left, dia)
        right, dia_right = self.depth(node.right, dia)
        dia = max(left + right, dia_left, dia_right)
        depth = max(left, right) + 1
        return depth, dia
    else:
        return 0, dia


# improve: use attribute dia, doesnt need to pass it around between two function
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def depth(p):
            if not p:
                return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans


# iterative, based on postorder
def diameterOfBinaryTree_2(self, root: TreeNode) -> int:
    stack, postorder, children_max_height = [root], {}, 0
    while stack and stack[-1]:
        node = stack[-1]  # check if children processed already
        if node.left and node.left not in postorder:
            stack.append(node.left)
        elif node.right and node.right not in postorder:
            stack.append(node.right)
        else:
            node = stack.pop()  # children are processed or no children, pop the stack
            left_height = postorder.get(node.left, 0)
            right_height = postorder.get(node.right, 0)
            postorder[node] = max(left_height, right_height) + 1  # 1 is node itself
            children_max_height = max(left_height + right_height, children_max_height)
    return children_max_height


# LC. 559 Maximum Depth of N-ary Tree

# recursive, DFS
def maxDepth_nary(self, root: "Node") -> int:
    # recursive
    if root:
        if root.children:
            depth = max([self.maxDepth(e) for e in root.children])
            # maybe better to use for generator?
        else:
            depth = 0
        return 1 + depth
    else:
        return 0


def maxDepth_nary_2(self, root: "Node") -> int:
    if root == None:
        return 0
    depth = 0
    for child in root.children:
        depth = max(depth, self.maxDepth(child))  # saving the depth array
    return depth + 1


# iterative, BFS
def maxDepth_nary_3(self, root):
    q, level = root and [root], 0
    while q:
        q, level = [child for node in q for child in node.children if child], level + 1
    return level


# LC. 104 Maximum Depth of Binary Tree
# recursive:
def maxDepth(self, root: TreeNode) -> int:
    if root:
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    else:
        return 0


# iterative based on postorder
def maxDepth_1(self, root: TreeNode) -> int:
    stack, depths = [(root, False)], {}
    if not root:
        return 0

    while stack:
        curr, visited = stack.pop()
        if visited:  # visited
            depths[curr] = 1 + max(depths.get(curr.left, 0), depths.get(curr.right, 0))
        else:  # not visited
            if curr:
                stack.append((curr, True))
                stack.append((curr.left, False))
                stack.append((curr.right, False))

    return depths[root]


#########################################################
#            Tree advanced property, LCA                #
#########################################################


#########################################################
#             Path - Root to Leaf                       #
#########################################################

# LC. 112 Path Sum
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    # root to leaf, better DFS
    # recursive or iterative?
    # which order? -- preoder -- easy with iterative

    if not root:
        return False

    stack, remain = [], {}
    stack = [root]
    remain[root] = sum

    while stack:
        node = stack.pop()
        if node:
            remain[node] -= node.val  # not sure
            if remain[node] == 0:
                if not (node.left or node.right):
                    return True
        if node.right:
            stack.append(node.right)
            remain[node.right] = remain[node]
        if node.left:
            stack.append(node.left)
            remain[node.left] = remain[node]

    return False


# recursive
def hasPathSum_1(self, root, sum):
    if not root:
        return False

    if not root.left and not root.right and root.val == sum:
        return True

    sum -= root.val

    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


# LC. 113 Path Sum II
# extend the hasPathSum iterative solution (but a lot of memory use.. can still improve)
# for example, instead of saving whole array in dict, You just need to save the parent node for children.
#
def pathSum(self, root: TreeNode, sum: int):
    if not root:
        return []

    stack, remain = [], {}
    stack = [root]
    remain[root] = [sum, [root.val]]
    res = []

    while stack:
        node = stack.pop()
        if node:
            remain[node][0] -= node.val  # not sure
            if remain[node][0] == 0:
                if not (node.left or node.right):
                    res.append(remain[node][1])
        if node.right:
            stack.append(node.right)
            remain[node.right] = [remain[node][0], remain[node][1] + [node.right.val]]
        if node.left:
            stack.append(node.left)
            remain[node.left] = [remain[node][0], remain[node][1] + [node.left.val]]

    return res


## someones solution using backtracking
class Solution_pathSum:
    def pathSum(self, root: TreeNode, sum: int):
        rst = []
        self._dfs(root, sum, rst, [])
        return rst

    def _dfs(self, root, sum, rst, path):
        if not root:
            return

        # add current root's value to the path
        path.append(root.val)

        # in case this is a leaf node
        if not root.left and not root.right:
            if not sum - root.val:
                # for primitive values, [:] is sufficient (although it is doing shallow copy)
                rst.append(path[:])
        else:
            self._dfs(root.left, sum - root.val, rst, path)
            self._dfs(root.right, sum - root.val, rst, path)

        # backtrack
        path.pop()


# LC. 129 Sum Root to Leaf Numbers

# LC. 257 Binary Tree Paths


#########################################################
#             Path - Any to Any Node Path               #
#########################################################
#
# LC. 437
# LC. 124
# LC. 543


#########################################################
#                 Reconstruct the Tree                  #
#########################################################
#
# LC. 114 Flatten Binary Tree to Linked List
def flatten(self, root: TreeNode):
    """
    Do not return anything, modify root in-place instead
    """
    if not root:
        return []

    stack = [root.right, root.left]
    while stack:
        node = stack.pop()
        if node:
            stack.append(node.right)
            stack.append(node.left)

            root.right = node
            root.left = None
            root = root.right


def __init__(self):
    self.prev = None


def flatten_1(self, root):
    if not root:
        return None
    self.flatten_1(root.right)
    self.flatten_1(root.left)

    root.right = self.prev
    root.left = None
    self.prev = root


# LC. 617
# LC. 226
# LC. 654

#########################################################
#                    AD HOC Problems                    #
#########################################################
# LC. 250
# LC. 863 All Nodes Distance K in Binary Tree


class Solution_863:
    def __init__(self):
        self.res = []

    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        # can go three directions: left, right, back
        # solution 1: create a dict to store the prev node
        # iterative
        lut, stack = {}, [root]
        lut[root] = None

        if not root:
            return []

        while stack and root:
            root = stack.pop()
            if root != target:
                if root.right:
                    lut[root.right] = root
                    stack.append(root.right)
                if root.left:
                    lut[root.left] = root
                    stack.append(root.left)
            else:
                break

        # find target, go down for k
        self.downK(root, K)

        # find target, go up for k (go up x, then go down k-x)

        while lut[root] and K > 0:
            if lut[root].left and lut[root].left == root:
                lut[root].left = None
            else:
                lut[root].right = None
            K -= 1
            root = lut[root]
            self.downK(root, K)

        return self.res

    # function that go down K
    def downK(self, root: TreeNode, K: int):
        if root:
            if K == 0:
                self.res += [root.val]
            else:
                self.downK(root.left, K - 1)
                self.downK(root.right, K - 1)


class Solution_863_2:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        conn = collections.defaultdict(list)

        def connect(parent, child):
            # both parent and child are not empty
            if parent and child:
                # building an undirected graph representation, assign the
                # child value for the parent as the key and vice versa
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            # in-order traversal
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        # the initial parent node of the root is None
        connect(None, root)
        # start the breadth-first search from the target, hence the starting level is 0
        bfs = [target.val]
        seen = set(bfs)
        # all nodes at (k-1)th level must also be K steps away from the target node
        for _ in range(K):
            # expand the list comprehension to strip away the complexity
            new_level = []
            for q_node_val in bfs:
                for connected_node_val in conn[q_node_val]:
                    if connected_node_val not in seen:
                        new_level.append(connected_node_val)
            bfs = new_level
            # add all the values in bfs into seen
            seen |= set(bfs)
        return bfs
