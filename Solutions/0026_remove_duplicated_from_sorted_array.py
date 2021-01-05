# 0026_remove_duplicated_from_sorted_array
# Easy
# Keys: #two_pointer #duplicates


class Solution:
    def removeDuplicates(self, nums) -> int:
        write_idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[write_idx]:
                write_idx += 1
                nums[write_idx] = nums[i]
        return write_idx + 1