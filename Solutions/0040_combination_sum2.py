# 0040_combination_sum2.py
# Medium
# Keys: #backtracking


class Solution:
    def combinationSum2_2(self, candidates, target: int):
        candidates.sort()
        output = []

        def helper(cand, targ, localList=[]):
            if targ == 0:
                output.append(list(localList))
                return
            for index, num in enumerate(cand):
                if targ - num < 0:
                    return
                if index > 0 and cand[index] == cand[index - 1]:
                    continue
                localList.append(num)
                helper(cand[index + 1 :], targ - num, localList)
                localList.pop()

        helper(candidates, target)
        return output

    def combinationSum2(self, candidates, target):
        # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return

        for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want
            # to count the first element in this recursive step even if it is the same
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])
