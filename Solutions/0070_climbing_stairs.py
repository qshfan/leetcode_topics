# 0070_climbing_stairs.py
# Easy
# Keys: #dp #recursion


class Solution:
    def climbStairs0(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

    # Top down + memoization (list)
    def climbStairs4(self, n):
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n - 1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)
        return dic[n]

    # Top down + memoization (dictionary)
    def __init__(self):
        self.dic = {1: 1, 2: 2}

    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dic[n]

    def climbStairs_dp(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]