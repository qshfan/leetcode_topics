# 0012_integer_to_roman
# Medium
# Keys: #math


class Solution:
    def intToRoman(self, num: int) -> str:
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return (
            m[num // 1000] + c[(num % 1000) // 100] + x[(num % 100) // 10] + i[num % 10]
        )

    def intToRoman_2(self, num: int) -> str:
        d = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        res = ""

        for i in d:
            res += (num // i) * d[i]
            num %= i

        return res