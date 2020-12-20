# Problem list:

# rotated sorted array
# 153. Find Minimum in Rotated Sorted Array
# 33. Search in Rotated Sorted Array
# 81. Search in Rotated Sorted Array II

# sorted array that has repeated values
# EPI 11.1 Search a sorted array for first occurrence of k
# 34. Find First and Last Position of Element in Sorted Array


class Solution_153:
    def findMin(self, A):
        left, right = 0, len(A) - 1
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] > A[right]:
                # minimum must be in A[mid + 1 : right + 1]
                left = mid + 1
            else:
                right = mid
        return A[left]


class Solution_33:
    def search(self, nums, target):
        L, H = 0, len(nums)
        while L < H:
            M = (L + H) // 2
            if target < nums[0] < nums[M]:  # -inf
                L = M + 1
            elif target >= nums[0] > nums[M]:  # +inf
                H = M
            elif nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1


class Solution_81:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True

            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1

            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


# EPI 11.1 Search a sorted array for first occurrence of k
def search_first_of_k(A, k):
    # Time O(logn)
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


# 34. Find First and Last Position of Element in Sorted Array
def searchRange(self, nums, target):
    def search(n):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo

    lo = search(target)
    return [lo, search(target + 1) - 1] if target in nums[lo : lo + 1] else [-1, -1]
