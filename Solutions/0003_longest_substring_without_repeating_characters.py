# 0003_longest_substring_without_repeating_characters
# Medium
# Keys: #hashmap #sliding_window #substring #pointer


class Solution:
    # slower
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        for index, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                # char already appeared in current non-repeating string
                # Key1: pay attention of the edge case, start<= or start<
                # Key2: using start pointer, saves the time of reconstruct the whole usedChar dict.
                start = usedChar[char] + 1
            else:
                maxLength = max(maxLength, index - start + 1)
            usedChar[char] = index
        return maxLength

    def lengthOfLongestSubstring_2(self, A: str) -> int:
        most_recent_occurrence = {}
        longest_dup_free_subarray_start_idx = result = 0

        for i, a in enumerate(A):
            if a in most_recent_occurrence:
                dup_idx = most_recent_occurrence[a]
                if dup_idx >= longest_dup_free_subarray_start_idx:
                    result = max(result, i - longest_dup_free_subarray_start_idx)
                    longest_dup_free_subarray_start_idx = dup_idx + 1
            most_recent_occurrence[a] = i
        return max(result, len(A) - longest_dup_free_subarray_start_idx)

    # using set
    def lengthOfLongestSubstring_3(self, s: str) -> int:
        longest = left = right = 0
        chars = set()
        while left < len(s) and right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1
        return longest