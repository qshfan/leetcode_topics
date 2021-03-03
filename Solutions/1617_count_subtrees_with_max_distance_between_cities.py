# 1617_count_subtrees_with_max_distance_between_cities
# Hard
# Keys: #backtracking #dfs

"""
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.
"""

# https://www.youtube.com/watch?v=KYorL6QSBek

import collections


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges):
        for i, (u, v) in enumerate(edges):
            edges[i] = [u - 1, v - 1]
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(source, mask):
            # mask: a subset of nodes [0 .. n-1]
            # return: farthest_point, distance(source, farthest)

            queue = collections.deque()
            queue.append([source, None, 0])
            while queue:
                node, par, d = queue.popleft()
                # change the problem to "counting the connected components"
                for nei in graph[node]:
                    if nei != par and mask >> nei & 1:
                        queue.append([nei, node, d + 1])
            return node, d

        ans = [0] * n

        for mask in range(1, 1 << n):
            edgecount = 0
            # is this subset of nodes (by 'mask') a subtree?
            for u, v in edges:
                if mask >> u & 1 and mask >> v & 1:
                    edgecount += 1
                    root = u

            # logic to calculate diameter of a graph
            # bfs twice if often used to find the diameter of tree
            if edgecount == bin(mask).count("1") - 1 != 0:
                # it is a subtree
                v, _ = bfs(root, mask)
                _, d = bfs(v, mask)
                ans[d] += 1
        return ans[1:]