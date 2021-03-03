# 0039_combination_sum.py
# Medium
# Keys: #backtracking #DFS


class Solution(object):
    # this template can be used in may backtracking / DFS problems
    # Time Complexity can be improved a lot if you don't loop after the target is negative.
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, nums, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], res)

    # faster solution
    def combinationSum_2(self, candidates, target):
        result = []
        candidates = sorted(candidates)

        def dfs(remain, stack):
            if remain == 0:
                result.append(stack)
                return

            for item in candidates:
                if item > remain:
                    break
                if stack and item < stack[-1]:
                    continue
                else:
                    dfs(remain - item, stack + [item])

        dfs(target, [])
        return result