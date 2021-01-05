# 0042_tapping_rain_water.py
# Hard
# Keys: #stack #double_path #two_pointer #dp #super_hard


class Solution:
    # use two pointer
    def trap(self, height) -> int:

        left = 0
        right = len(height) - 1
        max_water = 0
        leftmax = 0
        rightmax = 0

        while left <= right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if leftmax < rightmax:
                max_water += leftmax - height[left]
                # leftmax is smaller than rightmax, so the (leftmax-A[left]) water can be stored
                left += 1

            else:
                max_water += rightmax - height[right]
                right -= 1

        return max_water

    # use stack, reference to problems such as  Histogram, sunsetview, max water between columns, return max element in O(1) time in a stack (supporting pop and append)

    def trap_2(self, height) -> int:

        stack, res = [], 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()
                if stack:
                    res += (min(h, height[stack[-1]]) - height[bottom]) * (
                        i - stack[-1] - 1
                    )
            stack.append(i)
        return res

    # my version, failed solving
    def trap_3(self, height) -> int:
        def calculate_water(left_idx, right_idx):
            return min(height[left_idx], height[right_idx]) * (
                right_idx - left_idx - 1
            ) - sum(height[left_idx + 1 : right_idx])

        if len(height) == 0:
            return 0
        stack = [(height[0], 0)]
        water = {}

        for i in range(1, len(height)):
            left_height, left_idx = -1, -1
            while stack and height[i] >= stack[-1][0]:
                (left_height, left_idx) = stack.pop()
                # somehow calculate
            if left_idx >= 0:
                water[i] = calculate_water(left_idx, i)

                for j in range(left_idx + 1, i):
                    water[j] = 0
            stack.append((height[i], i))

        sum_v = sum(water.values())

        if stack:
            left_idx = stack.pop()[1]

        while stack:
            right_idx = left_idx
            left_idx = stack.pop()[1]
            print(left_idx, right_idx)
            sum_v += calculate_water(left_idx, right_idx)

        return sum_v