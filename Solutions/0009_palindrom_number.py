# 0009_palindrom_number.py
# Easy
# Keys: #math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        p, res = x, 0
        while p:
            res = res * 10 + p % 10
            p = p // 10
        return res == x

    def isPalindrome_2(self, x: int) -> bool:
        if x < 0:
            return False

        ranger = 1
        while x // ranger >= 10:
            ranger *= 10

        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) // 10
            ranger //= 100

        return True