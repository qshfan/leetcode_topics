# 0526_beautiful_arrangement
# Medium
# Keys: #backtracking #permutation
# related: LC46

"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15
"""
from functools import lru_cache


class Solution:
    # using dp, fast -- 状态压缩dp
    # https://leetcode-cn.com/problems/beautiful-arrangement/solution/zhuang-tai-ya-suo-dp-pythonban-by-daisykeepgoing/
    def countArrangement(self, N: int) -> int:
        # Question: do you need to use all the numbers from 1 to n to form each array?
        # Yes, otherwise n=2 has more than 2 answers.

        @lru_cache(None)
        def dfs(mask, i=1):
            if not mask:
                return 1
            return sum(
                dfs(mask ^ (1 << (n - 1)), i + 1)
                for n in range(1, N + 1)
                if mask & (1 << (n - 1)) and (not i % n or not n % i)
            )

        return dfs(2 ** N - 1)

    def countArrangement1(self, N: int) -> int:
        import functools

        @lru_cache(None)
        def dfs(i, cur):
            if i == N + 1:
                return 1
            res = 0
            for k in range(N):
                num = 1 << k
                if not cur & num and ((k + 1) % i == 0 or i % (k + 1) == 0):
                    res += dfs(i + 1, cur | num)
            return res

        return dfs(1, 0)

    # 全排列的写法 + 剪枝 --> 回溯
    # using backtrack, slow, time: O(2^n), space: O(n)
    def countArrangement2(self, N: int):
        self.ans = 0
        visited = [0] * (N + 1)

        def backtrack(path):
            if len(path) == N:
                self.ans += 1
                return
            for i in range(1, N + 1):
                if visited[i]:
                    continue
                if (len(path) + 1) % i != 0 and i % (len(path) + 1) != 0:
                    continue

                path.append(i)
                visited[i] = 1
                backtrack(path)
                visited[i] = 0
                path.pop()

        backtrack([])
        return self.ans