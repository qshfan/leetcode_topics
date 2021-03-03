# 1079_letter_tile_possibilities.py
# Medium
# Keys: #backtracking
from itertools import permutations


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()

        def dfs(path, t):
            if path:
                res.add(path)
            for i in range(len(t)):
                dfs(path + t[i], t[:i] + t[i + 1 :])

        dfs("", tiles)
        return len(res)

    # this version faster:
    def numTilePossibilities2(self, tiles):
        res = {""}
        for c in tiles:
            res |= {d[:i] + c + d[i:] for d in res for i in range(len(d) + 1)}
        return len(res) - 1

    def numTilePossibilities3(self, tiles: str) -> int:
        if len(tiles) == 1:
            return 1

        res = 0
        for i in range(1, len(tiles) + 1):
            res += len(set(permutations(tiles, i)))

        return res