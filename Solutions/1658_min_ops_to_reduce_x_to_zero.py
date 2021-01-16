# 1658_min_ops_to_reduce_x_to_zero.py
# Medium
# Keys: #greedy #prefix_sum #sliding_window #super_hard
# similar problems: 0918, 1423


from itertools import accumulate


class Solution:
    def minOperations(self, nums, x):
        cumsum = [0] + list(accumulate(nums))
        dic = {c: i for i, c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0:
            return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1

    def minOperations_2(self, nums, x):
        target, size, win_sum, lo, n = sum(nums) - x, -1, 0, -1, len(nums)
        for hi, num in enumerate(nums):
            win_sum += num
            while lo + 1 < n and win_sum > target:
                lo += 1
                win_sum -= nums[lo]
            if win_sum == target:
                size = max(size, hi - lo)
        return -1 if size < 0 else n - size