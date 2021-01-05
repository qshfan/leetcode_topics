# 0005_longest_palindromic_substring
# Medium
# Keys: #substring #palindrom #dp
# one difficulty is to deal with when palindrom has one char center or two char center


class Solution:
    # super slow version -- didnt use dp
    def longestPalindrome(self, s: str) -> str:
        def get_max_palindrom(s, left, right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return s[left + 1 : right]

        maxlen = 0
        res = ""
        for i in range(len(s)):
            s1 = get_max_palindrom(s, i, i)
            if len(s1) >= maxlen:
                maxlen = len(s1)
                res = s1
            s2 = get_max_palindrom(s, i, i + 1)
            if len(s2) >= maxlen:
                maxlen = len(s2)
                res = s2

        return res

    # 10 times faster -- DP solution
    # Use start and maxlen, only react when the maxlen is larger than recorded.
    # for each element, look back maxlen + 1 postions, check if it is palindrom
    # this will not missing the array, because you can keep extending when you moving right
    # (skip left, check from right side)
    def longestPalindrome_2(self, s: str) -> str:
        maxlen, start = 0, 0
        for i in range(len(s)):
            # deal with the case when maxlen increase by two elements
            if (
                i - maxlen >= 1
                and s[i - maxlen - 1 : i + 1] == s[i - maxlen - 1 : i + 1][::-1]
            ):
                start = i - maxlen - 1
                maxlen += 2
                continue
            # deal with when maxlen incfease by one element
            if i - maxlen >= 0 and s[i - maxlen : i + 1] == s[i - maxlen : i + 1][::-1]:
                start = i - maxlen
                maxlen += 1
        return s[start : start + maxlen]

    # 20 times faster -- basic same idea as earlier, slightly difference, doesnt matter
    def longestPalindrome_3(self, s: str) -> str:
        str_len = len(s)
        if str_len < 2 or s == s[::-1]:
            return s
        start, max_len = 0, 1
        for i in range(1, str_len):
            odd_start = i - max_len - 1
            even_start = i - max_len
            odd = s[odd_start : i + 1]
            even = s[even_start : i + 1]
            if odd_start >= 0 and odd == odd[::-1]:
                start = odd_start
                max_len += 2
            elif even_start >= 0 and even == even[::-1]:
                start = even_start
                max_len += 1
        return s[start : start + max_len]
