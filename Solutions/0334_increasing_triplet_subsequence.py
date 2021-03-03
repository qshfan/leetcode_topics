# 0334_increasing_triplet_subsequence
# Medium
# Keys: #binary_search #subsequence

# Using EAFP (easier to ask for forgiveness than permission):

import bisect


def increasingSubsequence(self, nums, k):
    try:
        inc = [float("inf")] * (k - 1)
        for x in nums:
            inc[bisect.bisect_left(inc, x)] = x
        return k == 0
    except:
        return True


# Using LBYL (look before you leap):


def increasingSubsequence_2(self, nums, k):
    inc = [float("inf")] * (k - 1)
    for x in nums:
        i = bisect.bisect_left(inc, x)
        if i >= k - 1:
            return True
        inc[i] = x
    return k == 0


"""
Start with the maximum numbers for the first and second element. Then:
(1) Find the first smallest number in the 3 subsequence
(2) Find the second one greater than the first element, reset the first one if it's smaller
"""


def increasingTriplet_3(nums):
    first = second = float("inf")
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False