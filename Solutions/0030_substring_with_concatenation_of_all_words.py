# 0030_substring_with_concatenation_of_all_words
# Hard
# Keys: #two_pointer #hashmap #duplicates
# Reference: LC 0003

import collections


class Solution:
    # own solution, not optimal
    # Time O(n*m) Space O(m) (m is the number of words in words)
    def findSubstring(self, s: str, words):
        word_dict = {}
        for i, word in enumerate(words):
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

        res = []
        len_words = len(words)
        len_word = len(words[0])
        sum_len = len_words * len_word

        def is_concat(piece):
            i = 0
            seen = word_dict.copy()
            while i < sum_len:
                word = piece[i : i + len_word]
                if word in seen:
                    seen[word] -= 1
                    if seen[word] < 0:
                        return False
                else:
                    return False
                i += len_word
            return True

        for i in range(len(s) - sum_len + 1):
            piece = s[i : i + sum_len]
            if is_concat(piece):
                res.append(i)

        return res

    # also faster record the seen word, reference to LC 3, more complicated, because words can repeat
    def findSubstring_3(self, s: str, words):
        c = collections.Counter(words)
        m = len(words)
        n = len(words[0])
        res = []

        # Loop over word length
        for i in range(n):
            left = i
            subd = collections.defaultdict(int)
            count = 0
            # Loop over the string
            for j in range(i, len(s) - n + 1, n):
                # Get a word from observed substring
                word = s[j : j + n]
                # check if it is a valid word
                if word in c:
                    subd[word] += 1
                    count += 1
                    ##Shift the window as long as we have encountered more number of a word than is needed
                    ##Note that we can shift the window by word length directly as the outer loop is there to
                    ##make sure that anything is not missed out
                    ##This solution will give indices out of order by OJ accepts it.
                    while subd[word] > c[word]:
                        subd[s[left : left + n]] -= 1
                        left += n
                        count -= 1
                    ##Count will be equal to m only when we all the words are read the exact number of times needed
                    if count == m:
                        res.append(left)
                # If is not a valid word then just skip over the current word (Don't worry about the middle characters
                ##outer loop will take care of it)
                else:
                    left = j + n
                    subd = collections.defaultdict(int)
                    count = 0

        return res

    # faster
    def findSubstring_2(self, s: str, words):
        ans = []
        target = collections.Counter(words)
        if not target:
            return ans

        size = len(words[0])
        for start in range(size):
            need = {}
            l = start
            for r in range(start, len(s), size):
                w = s[r : r + size]
                if w not in target:
                    need = {}
                    l = r + size
                    continue
                # if found repeated word, update l to the last seen + 1
                if need and w not in need:
                    tmp = s[l : l + size]
                    while tmp != w:
                        need[tmp] += 1
                        l += size
                        tmp = s[l : l + size]
                    l += size
                    continue

                if not need:
                    need = target.copy()
                need[w] -= 1

                # if found word, delete from need
                if need[w] == 0:
                    del need[w]

                # if found, search for farthest word
                if not need:
                    ans.append(l)
                    need[s[l : l + size]] += 1
                    l += size
        return ans
