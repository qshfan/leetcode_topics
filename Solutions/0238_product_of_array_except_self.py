# 0238_product_of_array_except_self
# Medium
# Keys #math #double_pass

from itertools import accumulate
from operator import mul


class Solution:
    def productExceptSelf(self, values):
        products_left = list(accumulate(values, mul, initial=1))[:-1]
        products_right = list(accumulate(values[:0:-1], mul, initial=1))[::-1]
        return list(map(mul, products_left, products_right))

    # one solution explains very well with pictures
    # https://leetcode-cn.com/problems/product-of-array-except-self/solution/gan-jue-da-bu-fen-ti-jie-du-shi-tie-dai-ma-jia-fu-/

    # not opitmized space
    def productExceptSelf_0(self, nums):
        n = len(nums)
        l, r = [1] * n, [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]
        res = []
        for i in range(n):
            res.append(l[i] * r[i])
        return res

    # with optimized space
    def productExceptSelf_1(self, nums):
        n = len(nums)
        l = [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
        r = 1
        for i in range(n - 1, -1, -1):
            l[i] *= r
            r *= nums[i]
        return l

    def productExceptSelf_2(self, nums):

        prod = 1
        prodvalues = []
        for i in range(0, len(nums)):
            prodvalues.insert(i, prod)
            prod = prod * nums[i]

        prod = 1
        for j in range(len(nums) - 1, -1, -1):

            prodvalues[j] = prod * prodvalues[j]
            prod = prod * nums[j]

        return prodvalues

    def productExceptSelf_3(self, nums):

        # The length of the input array
        length = len(nums)

        # The left and right arrays as described in the algorithm
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):

            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):

            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]

        return answer

    def productExceptSelf_4(self, nums):

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer