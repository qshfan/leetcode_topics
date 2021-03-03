# 0047_permutations2
# Medium
# Keys： #backtracking #permutation

"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10


思路
回溯+剪枝/去重，去重则要求排序，便于剪枝

回溯问题三要素：
有效结果；回溯范围及答案更新；剪枝条件。
# https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
"""


class Solution:
    def permuteUnique(self, nums):
        # res用来存放结果
        if not nums:
            return []
        res = []
        used = [0] * len(nums)

        def backtracking(nums, used, path):
            # 终止条件
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtracking(nums, used, path)
                    path.pop()
                    used[i] = 0

        # 记得给nums排序
        backtracking(sorted(nums), used, [])
        return res

    def permuteUnique2(self, nums):
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]

        self.backtrack([], nums, check)
        return self.res

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0

    def permuteUnique3(self, nums, sofar=[[]]):
        if not nums:
            return sofar
        num = nums.pop()
        ans = []
        for perm in sofar:
            slot = len(perm) - 1
            while slot >= 0 and perm[slot] != num:
                ans.append(perm[:slot] + [num] + perm[slot:])
                slot -= 1
            ans.append(perm + [num])
        return self.permuteUnique3(nums, ans)