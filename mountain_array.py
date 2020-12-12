"""
This collection contains Leetcode problems related with "Mountain Array".
* LC 162. Find Peak Element (Medium)
* LC 845. Longest Mountain in Array (Medium)
* LC 852. Peak Index in a Mountain Array (Easy)
* LC 941. Valid Mountain Array (Easy)
* LC 1095. Find in Mountain Array (Hard)
* LC 1671. Minimum Number of Removals to Make Mountain Array (Hard)

In the code I will sort these problems by difficulty.
"""

# LC 941. Valid Mountain Array (Easy)
# "if two people climb from both side, they will meet"
def validMountainArray(arr):
    i, j, n = 0, len(arr) - 1, len(arr)
    while i + 1 < n and arr[i] < arr[i + 1]: i += 1
    while j > 0 and arr[j - 1] > arr[j]: j -= 1
    return 0 < i == j < n - 1

# Another way is to use uphill as a flag. 
# This code offers a way to detect the turning point of uphill
def validMountainArray_1(arr):
    if len(arr)<3 or arr[0]>=arr[1]:
        return False
    uphill = True
    for i in range(1,len(arr)):
        if uphill:
            if arr[i-1]>=arr[i]:
                uphill = False
        if not uphill:
            if arr[i-1]<=arr[i]:
                return False
    return not uphill

# LC 852. Peak Index in a Mountain Array
# The array is "guaranteed to be a mountain array" --> peak exist.
def peakIndexInMountainArray(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] < 0:
            return i

# use arr.index(value)  - applies when value is guaranteed unique. 
def peakIndexInMountainArray_1(arr):
    return arr.index(max(arr))

# LC 845. Longest Mountain in Array (Medium)
def longestMountain(A):
    up, down = [0] * len(A), [0] * len(A)
    for i in range(1, len(A)):
        if A[i] > A[i - 1]: up[i] = up[i - 1] + 1
    for i in range(len(A) - 1)[::-1]:
        if A[i] > A[i + 1]: down[i] = down[i + 1] + 1
    return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])
    



# LC 1095. Find in Mountain Array (Hard)


# LC 1671. Minimum Number of Removals to Make Mountain Array (Hard)


#LC 162 Find Peak Element (Medium)
# This problem is simple but has very poor description on edge cases. I would skip it. 
def findPeakElement(nums):
    for i in range(1, len(nums) - 1):
        if nums[i-1] < nums[i] > nums[i+1]:
            return i
    return len(nums) - 1  if nums[-1] > nums[0] else 0