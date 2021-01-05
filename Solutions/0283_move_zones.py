# 0283_move_zones.py
# Easy
# Keys: #two_pointer #duplicates


class Solution:
    # use swaping, two pointer
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeroes = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[numZeroes] = nums[numZeroes], nums[i]
                numZeroes += 1

    # used only one pointer
    def moveZeroes_2(self, nums) -> None:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        nums[idx:] = [0] * len(nums[idx:])
