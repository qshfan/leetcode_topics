# 0240_search_2d_matrix_2
# Keys: 2d_array
class Solution:
    def searchMatrix(self, A, x: int) -> bool:
        row, col = 0, len(A[0]) - 1
        while row < len(A) and col >= 0:
            if x > A[row][col]:
                row += 1
            elif x == A[row][col]:
                return True
            else:
                col -= 1
        return False