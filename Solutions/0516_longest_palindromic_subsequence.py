# 0516_longest_palindromic_subsequence.py
# Medium
# Keys: #dp #subsequence


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0 for j in range(n)]
        dp[n - 1] = 1

        for i in range(n - 1, -1, -1):  # can actually start with n-2...
            newdp = dp[:]  # This is to make copy of the array
            newdp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j - 1]
                else:
                    newdp[j] = max(dp[j], newdp[j - 1])
            dp = newdp

        return dp[n - 1]

    def longestPalindromeSubseq_2(self, s: str) -> int:
        n = len(s)
        dp = [[1] * 2 for _ in range(n)]
        for j in range(1, len(s)):
            for i in reversed(range(0, j)):
                if s[i] == s[j]:
                    dp[i][j % 2] = 2 + dp[i + 1][(j - 1) % 2] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j % 2] = max(dp[i + 1][j % 2], dp[i][(j - 1) % 2])
        return dp[0][(n - 1) % 2]