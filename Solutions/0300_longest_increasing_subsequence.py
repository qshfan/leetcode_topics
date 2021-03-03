# 0300_longest_increasing_subsequence.py
# Medium
# Keys: #dp #binary_search #subsequence

# best explaination:
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/429079/Python-5-Approaches%3A-Recursion-Recur-%2B-Memo-DP-DP-%2B-Binary-Search-Print-all-LIS

# class Solution:
def lengthOfLIS(nums):
    tails = [0] * len(nums)
    size = 0
    for num in nums:
        l, r = 0, size
        while l != r:
            m = l + (r - l) // 2
            if tails[m] < num:
                l = m + 1
            else:
                r = m
        tails[l] = num
        print(tails)
        size = max(size, l + 1)
    return size


arr = [10, 9, 2, 5, 1, 7, 101, 18]
lengthOfLIS(arr)


def lengthOfLIS_2(nums):
    if not nums:
        return 0
    N = len(nums)
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)