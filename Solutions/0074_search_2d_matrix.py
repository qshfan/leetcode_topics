# 0074_search_2d_matrix
# Keys: 2d_array

import bisect


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        return (
            bool(matrix) and target in matrix[bisect.bisect(matrix, [target + 0.5]) - 1]
        )
