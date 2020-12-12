# Practices according to post:
# https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns#Decision-Making

##################
# Min / Max Path #
##################
# LC 746 Min Cost Climbing Stairs -->> Easy
# lower, low can be replaced by dp[]
def minCostClimbingStairs(self, cost):
    curr_lower, curr_low = 0, 0
    for i in range(2, len(cost) + 1):
        curr = min((curr_lower + cost[i - 2]), (curr_low + cost[i - 1]))
        curr_lower, curr_low = curr_low, curr
    return curr


#################
# Distinct Ways #
#################

# LC 70 Climbing Stairs -->> Easy
def climbStairs(self, n: int):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


#####################
# Merging Intervals #
#####################

# LC 96. Unique Binary Search Trees
def numTrees(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(1, n + 1):
        res = 0
        for j in range(i):
            res += dp[j] * dp[i - j - 1]
        dp[i] = res
    return res


#################
# DP on Strings #
#################

# LC 516. Longest Palindromic Subsequence  -->> Medium
def longestPalindromeSubseq(s):
    # Time: O(n2)
    if s == s[::-1]:
        return len(s)

    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def longestPalindromeSubseq_1(s):
    # Time O(n)
    if s == s[::-1]:
        return len(s)

    n = len(s)
    dp = [0 for j in range(n)]
    dp[n - 1] = 1

    for i in reversed(range(n - 1)):  # can actually start with n-2...
        newdp = dp[:]

        newdp[i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                newdp[j] = 2 + dp[j - 1]
            else:
                newdp[j] = max(dp[j], newdp[j - 1])
        dp = newdp

    return dp[n - 1]


###################
# Decision Making #
###################

# Include a few problems to buy and sell stocks

# 121. Best Time to Buy and Sell Stock  -->> Easy
# Use Kadane's Algorithm. Same problem in EPI
def maxProfit(prices):
    maxCur, maxSoFar = 0, 0
    for i in range(1, len(prices)):
        maxCur += prices[i] - prices[i - 1]
        maxCur = max(0, maxCur)
        maxSoFar = max(maxCur, maxSoFar)
    return maxSoFar