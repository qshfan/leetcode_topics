# 0215_kth_largest_element_in_array.py
# Medium
# keys: #heap #divide_conquer # quicksort
import operator, random, heapq


class Solution:
    # solution 1: use heap. pros: use python standard lib, fast; cons: did more than needed
    def findKthLargest_0(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    # solution 2: pivot at kth position
    def findKthLargest(self, A, k):
        def find_kth(comp):
            def partition_around_pivot(left, right, pivot_idx):
                pivot_value = A[pivot_idx]
                print(A[pivot_idx])
                j = left
                # pivid is random, but we want to reuse the code, swap
                A[pivot_idx], A[right] = A[right], A[pivot_idx]
                for i in range(left, right):
                    if comp(A[i], pivot_value):
                        A[i], A[j] = A[j], A[i]
                        j += 1
                A[right], A[j] = A[j], A[right]
                return j

            left, right = 0, len(A) - 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                new_pivot_index = partition_around_pivot(left, right, pivot_idx)
                if new_pivot_index == k - 1:
                    return A[new_pivot_index]
                elif new_pivot_index > k - 1:
                    right = new_pivot_index - 1
                else:
                    left = new_pivot_index + 1

        return find_kth(operator.gt)

    def findKthLargest_2(self, arr, k):
        """
        :type arr: list of int
        :type k: int
        :rtype: int
        """
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            choosen_pivot_index = random.randint(left, right)

            final_index_of_choosen_pivot = self.partition(
                arr, left, right, choosen_pivot_index
            )

            if final_index_of_choosen_pivot == n - k:
                return arr[final_index_of_choosen_pivot]
            elif final_index_of_choosen_pivot > n - k:
                right = final_index_of_choosen_pivot - 1
            else:
                left = final_index_of_choosen_pivot + 1

        return -1

    def partition(self, arr, left, right, pivot_index):
        pivot_value = arr[pivot_index]
        lesser_items_tail_index = left

        self.swap(arr, pivot_index, right)

        for i in range(left, right):
            if arr[i] < pivot_value:
                self.swap(arr, i, lesser_items_tail_index)
                lesser_items_tail_index += 1

        self.swap(arr, right, lesser_items_tail_index)
        return lesser_items_tail_index

    def swap(self, arr, first, second):
        temp = arr[first]
        arr[first] = arr[second]
        arr[second] = temp