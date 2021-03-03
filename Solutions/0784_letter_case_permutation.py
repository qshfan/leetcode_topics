# 0784_letter_case_permutation.py
# Medium
# Keys: #backtracking ##bit_manipulation

import itertools


class Solution:
    def letterCasePermutation(self, S: str):
        self.res = []
        self.dfs(S, "", 0)
        return self.res

    def dfs(self, S, path, index):
        if index == len(S):
            self.res.append(path)
            return

        if S[index].isalpha():
            self.dfs(S, path + S[index].lower(), index + 1)
            self.dfs(S, path + S[index].upper(), index + 1)
        else:
            self.dfs(S, path + S[index], index + 1)

    def letterCasePermutation_2(self, S: str):
        results = [S]

        for i in range(len(S)):
            c = S[i]

            if "0" <= c <= "9":
                continue

            n = len(results)
            for j in range(n):
                s = results[j]

                if "a" <= c <= "z":
                    new_C = c.upper()
                else:
                    new_C = c.lower()

                results.append(s[:i] + new_C + s[i + 1 :])

        return results

    def letterCasePermutation_3(self, S: str):
        perms = [""]
        for c in S:
            if c.isdigit():
                perms = [pref + c for pref in perms]
            else:
                perms = [pref + ch for pref in perms for ch in [c.lower(), c.upper()]]

        return perms

    def letterCasePermutation_4(self, S):
        res = [""]
        for ch in S:
            if ch.isalpha():
                res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i + ch for i in res]
        return res

    def letterCasePermutation_5(self, S):
        L = [set([i.lower(), i.upper()]) for i in S]
        return map("".join, itertools.product(*L))

    def letterCasePermutation_6(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                res.extend([s[:i] + s[i].swapcase() + s[i + 1 :] for s in res])
        return res