# 0652_find_duplicate_subtrees
# Medium
# keys #DFS #recursion #serialization #hashing

import collections

# sample solution of python2
def findDuplicateSubtrees(self, root):
    def trv(root):
        if not root:
            return "null"
        struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
        nodes[struct].append(root)
        return struct

    nodes = collections.defaultdict(list)
    trv(root)
    return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]


# sample solution 2
def findDuplicateSubtrees_2(self, root):
    from hashlib import sha256

    def hash_(x):
        S = sha256()
        S.update(x)
        return S.hexdigest()

    def merkle(node):
        if not node:
            return "#"
        m_left = merkle(node.left)
        m_right = merkle(node.right)
        node.merkle = hash_(m_left + str(node.val) + m_right)
        count[node.merkle].append(node)
        return node.merkle

    count = collections.defaultdict(list)
    merkle(root)
    return [nodes.pop() for nodes in count.values() if len(nodes) >= 2]