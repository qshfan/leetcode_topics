# 0028_strstr.py
# Easy
# Keys: #two_pointer #strOps


class Solution:
    # when you slicing the string, you are creating a copy of the string.
    # Time: O(n*m), Space: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i, char in enumerate(haystack):
            if char == needle[0] and i <= len(haystack) - len(needle):
                if haystack[i : (i + len(needle))] == needle:
                    return i

        return -1

    # shorter
    def strStr_2(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    # using python function .find()
    def strStr_3(self, haystack, needle):
        return haystack.find(needle)
