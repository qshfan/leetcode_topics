# 1712_ways_split_array_to_three_subarrays.py
# Medium
# keys: #super_hard #prefix_sum #binary_search
from itertools import accumulate


class Solution:
    def waysToSplit(self, nums):
        MOD = 10 ** 9 + 7
        P = list(accumulate(nums, initial=0))
        S = sum(nums)

        ans = 0
        j1 = j2 = 0
        # Pi <= Pj - Pi <= S - Pj
        # 2Pi <= Pj and 2Pj <= S
        for i in range(1, len(P)):
            j1 = max(j1, i + 1)
            while j1 < len(P) and 2 * P[i] > P[j1]:
                j1 += 1
            j2 = max(j2, j1)
            while j2 < len(P) - 1 and 2 * P[j2] <= S + P[i]:
                j2 += 1
            ans += j2 - j1

        return ans % MOD