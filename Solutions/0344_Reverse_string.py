# 0344_Reverse_string.py
# Easy
# keys: #recursion #strOps
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)

    def reverseString2(self, s):
        s.reverse()