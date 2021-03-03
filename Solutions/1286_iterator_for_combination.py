# 1286_iterator_for_combination.py
# Medium
# Keys: #design #backtracking #bit_manipulation

# few ways:
# change the string to bitmask: 111000 for "abcdef, 3", find the next biggest number that has 3 1s

# solution by @vicy_100
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.n = len(characters)
        self.combinations = gen_combinations(self.n, combinationLength)
        self.ind = len(self.combinations) - 1

    def next(self) -> str:
        s = ""
        for i in range(self.n):
            if self.combinations[self.ind][i] != "0":
                s += self.characters[i]
        self.ind -= 1
        return s

    def hasNext(self) -> bool:
        return self.ind > -1


def gen_combinations(l, n):
    end = int("1" * l, 2)
    ans = []
    for i in range(end + 1):
        b = bin(i)[2:]
        if b.count("1") == n:
            ans.append(b.zfill(l))
    return ans


# second way: work on string
# i also came to the init and hasNext function, but not sure how to keep track to find the next one.
# in the end, i think the bit mask solution fits better this problem
# solution by @DB...
from os.path import commonprefix


class CombinationIterator2:
    def __init__(self, characters, combinationLength):
        self.c = characters
        self.len = combinationLength
        self.state = ""

    def next(self):
        if self.state == "":
            self.state = self.c[: self.len]
        else:
            end = len(commonprefix([self.c[::-1], self.state[::-1]]))
            place = self.c.index(self.state[-end - 1])
            self.state = self.state[: -end - 1] + self.c[place + 1 : place + 2 + end]
        return self.state

    def hasNext(self):
        return self.state != self.c[-self.len :]


# use backtracking to create the permute bit mask
class CombinationIterator3:
    """
    bit mask, 2^15
    Eg: "abc", 2
    We start with "111" which is 7. Run a loop over 0 to 7 both inclusive. The possible values with 2 set bits are ["011", "101", "110"]
    """

    def __init__(self, characters: str, combinationLength: int):
        # sorted & distinct, so permutation would gurantee the lexicographical order.
        self.characters = characters
        self.n = combinationLength
        self.i = 0
        self.res = []
        self.permute("", 0)

    def permute(self, s, start):
        if len(s) == self.n:
            self.res.append(s)
            return
        for i in range(start, len(self.characters)):
            self.permute(s + self.characters[i], i + 1)  # take char[i]

    def next(self) -> str:
        res = self.res[self.i]
        self.i += 1
        # print(self.res)
        return res

    def hasNext(self) -> bool:
        return self.i < len(self.res)