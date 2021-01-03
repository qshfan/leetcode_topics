# 0001_two_sum
# Easy
# Keys: #hashmap
class Solution:
    def twoSum(self, nums, target: int):
        dictA = {}

        for i, el in enumerate(nums):
            if target - el in dictA.keys():
                return [dictA[target - el], i]

            else:
                dictA.update({el: i})
