# 0131_palindrome_partitioning.py
# Medium
# Keys: #backtracking #dp #dfs

import functools, itertools


class Solution:
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)  # key of the solution

    def isPal(self, s):
        return s == s[::1]

    # use cache to speed up
    def partition2(self, s):
        @functools.lru_cache(len(s))  # would this perform memoization?
        def dfs2(start):
            if start == len(s):
                return [[]]
            res = []
            for i in range(start, len(s)):
                cur = s[start : i + 1]
                if cur == cur[::-1]:
                    res += [[cur] + rest for rest in dfs2(i + 1)]
            return res

        return dfs2(0)

    # solution with dp
    def partition_dp(self, s):
        def find_all_palindromes(s):
            B = [0] * (2 * n)
            for i, j in itertools.combinations_with_replacement(range(n), 2):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    B[i + j + 1] = max(B[i + j + 1], j - i + 1)
            return B

        n = len(s)
        B = find_all_palindromes(s)

        dp = [[] for _ in range(n + 1)]
        dp[0] = [[]]
        for i in range(0, n):
            for k in range(0, i + 1):
                if B[2 * i - k + 1] >= k:
                    for elem in dp[i - k]:
                        dp[i + 1].append(elem + [s[i - k : i + 1]])

        return dp[-1]