# 1415_kth_happy_string.py
# Medium
# keys: #backtracking #dfs


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.res = ""
        self.n = n
        self.k = k

        def dfs(cur, tmp):
            if len(cur) == self.n:
                self.k -= 1
                if self.k == 0:
                    self.res = cur
                    return
                return
            for i in tmp:
                if self.res:
                    return self.res
                new_tmp = [j for j in ["a", "b", "c"] if j != i]
                dfs(cur + i, new_tmp)

        dfs("", ["a", "b", "c"])
        return self.res