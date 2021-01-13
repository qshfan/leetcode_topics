# 0881_boats_to_save_people.py
# Medium
# Keys: #greedy #two_pointer


class Solution:
    # my solution
    def numRescueBoats(self, people, limit: int):
        # greedy
        boat = 0
        people.sort(reverse=True)
        left, right = 0, len(people) - 1

        while left < right:  # trivial: can left==right? what about example 3?
            space = limit - people[left]
            if people[right] <= space:
                right -= 1
            boat += 1
            left += 1

        if right == left:
            boat += 1
        return boat

    def numRescueBoats_1(self, people, limit):
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i