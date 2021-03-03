# 0797_all_paths_from_source_to_target.py
# Medium
# keys: #recursion #backtracking


class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])

        res = []
        dfs(0, [0])
        return res

    def allPathsSourceTarget2(self, graph, cur=0):
        if cur == len(graph) - 1:
            return [[len(graph) - 1]]
        return [
            ([cur] + path)
            for i in graph[cur]
            for path in self.allPathsSourceTarget2(graph, i)
        ]

    def allPathsSourceTarget3(self, graph):
        def dfs(formed):
            if formed[-1] == n - 1:
                sol.append(formed)
                return
            for child in graph[formed[-1]]:
                dfs(formed + [child])

        sol, n = [], len(graph)
        dfs([0])
        return sol
