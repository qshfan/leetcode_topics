# 0014_longest_common_prefix
# Easy
# Keys: #strOps


class Solution:
    # by default, the max/min to an array of strings will return according to alphebetic order
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        # since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]  # stop until hit the split index
        return s1

    # but you can also set the key of min/max to length of string, thus get the shortest/longest string
    def longestCommonPrefix_2(self, strs) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

    def longestCommonPrefix_3(self, strs) -> str:
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1:
                break
            ret += c[0]
        return ret
