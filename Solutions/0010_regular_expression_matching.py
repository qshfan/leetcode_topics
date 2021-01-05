# 0010_regular_expression_matching
# Hard
# Keys #strOps #dp #backtracking #super_hard
class Solution:

    cache = {}

    def isMatch(self, s: str, p: str) -> bool:

        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s
        if p[-1] == "*":
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == ".") and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == ".") and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False

    def isMatch_2(self, s: str, p: str) -> bool:
        dp = [[True] + [False] * len(s)]
        for i, pc in enumerate(p):
            row = [pc == "*" and dp[-2][0]]
            for j, sc in enumerate(s):
                if pc == ".":
                    row.append(dp[-1][j])
                elif pc == "*":
                    row.append(
                        dp[-2][j + 1]
                        or ((p[i - 1] == "." or p[i - 1] == sc) and row[j])
                    )
                else:
                    row.append(dp[-1][j] and pc == sc)
            dp.append(row)
        return dp[-1][-1]

    def isMatch_3(self, s: str, p: str) -> bool:

        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == "*"
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == "*":
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == ".":
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == ".")
        return dp[-1][-1]