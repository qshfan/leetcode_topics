# 0004_median_two_sorted_array
# Hard
# Keys: #binary_search #divide_conquer #odd_even_partition #sorted_array #super_hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).

# a good reference:
# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation

# This problem is notoriously hard to implement due to all the corner cases. Most implementations consider odd-lengthed and even-lengthed arrays as two different cases and treat them separately. As a matter of fact, with a little mind twist. These two cases can be combined as one, leading to a very simple solution where (almost) no special treatment is needed.

# First, let's see the concept of 'MEDIAN' in a slightly unconventional way. That is:

# "if we cut the sorted array to two halves of EQUAL LENGTHS, then
# median is the AVERAGE OF Max(lower_half) and Min(upper_half), i.e. the
# two numbers immediately next to the cut".


class Solution:
    # Using python sorted:
    # complexity is depend on python sorted, for sorted array, it is O(min(m, n))
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        data = sorted(nums1 + nums2)
        mid = len(data) // 2
        return (data[mid] + data[-mid - 1 :][0]) / 2

    # iterative solution
    def findMedianSortedArrays_2(self, nums1, nums2) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        min_index, max_index = 0, m

        while min_index <= max_index:
            i = int((min_index + max_index) / 2)
            j = int((m + n + 1) / 2 - i)

            if i < m and j > 0 and nums2[j - 1] > nums1[i]:
                min_index = i + 1
            elif i > 0 and j < n and nums2[j] < nums1[i - 1]:
                max_index = i - 1
            else:
                if i == 0:
                    median = nums2[j - 1]
                elif j == 0:
                    median = nums1[i - 1]
                else:
                    median = max(nums1[i - 1], nums2[j - 1])
                break

        if (m + n) % 2 == 1:
            return median
        if i == m:
            return (median + nums2[j]) / 2.0
        if j == n:
            return (median + nums1[i]) / 2.0

        return (median + min(nums1[i], nums2[j])) / 2.0

    # recursive solution: change the median problem to kth largest element problem
    def findMedianSortedArrays_3(self, nums1, nums2) -> float:

        l = len(nums1) + len(nums2)
        return (
            self.findKth(nums1, nums2, l // 2)
            if l % 2 == 1
            else (
                self.findKth(nums1, nums2, l // 2 - 1)
                + self.findKth(nums1, nums2, l // 2)
            )
            / 2.0
        )

    # find the kth element int the two sorted arrays
    # let us say: A[aMid] <= B[bMid], x: mid len of a, y: mid len of b, then wen can know
    #
    # (1) there will be at least (x + 1 + y) elements before bMid
    # (2) there will be at least (m - x - 1 + n - y) = m + n - (x + y +1) elements after aMid
    # therefore
    # if k <= x + y + 1, find the kth element in a and b, but unconsidering bMid and its suffix
    # if k > x + y + 1, find the k - (x + 1) th element in a and b, but unconsidering aMid and its prefix
    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1:
            return nums2[k]
        if k == len(nums1) + len(nums2) - 1:
            return max(nums1[-1], nums2[-1])
        i = len(nums1) // 2
        j = k - i
        if nums1[i] > nums2[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(nums1[:i], nums2[j:], i)
        else:
            return self.findKth(nums1[i:], nums2[:j], j)
