# 0027_remove_element
# Easy
# Keys: #two_pointer #duplicates


class Solution:
    def removeElement(self, nums, val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx