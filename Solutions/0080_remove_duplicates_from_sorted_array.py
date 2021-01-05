# 0080_remove_duplicates_from_sorted_array
# Medium
# Keys: #two_pointer #duplicates


class Solution:
    def removeDuplicates(self, nums) -> int:
        j, count = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1

        return j

    # short -- changed a little bit the approach, instead of counting and compare with n-1, directly compare with n-2
    def removeDuplicates_2(self, nums) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i