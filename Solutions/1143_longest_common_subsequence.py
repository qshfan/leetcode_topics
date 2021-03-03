# 1143_longest_common_subsequence.py
# Medium
# Keys: #dp #subsequence


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if s == s[::-1]:
        #     return len(s)

        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for j in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]