# Keys: #easy #hashmap #neat


class Solution:
    # My soluton:
    def canFormArray(self, arr, pieces):
        idx_map = {num: i for i, num in enumerate(arr)}
        for piece in pieces:
            if (
                piece[0] not in idx_map
                or piece != arr[idx_map[piece[0]] : idx_map[piece[0]] + len(piece)]
            ):
                return False
        return True

    # better version
    def canFormArray_2(self, arr, pieces):
        for piece in pieces:
            try:
                idx = arr.index(piece[0])
            except:
                return False
            if arr[idx : idx + len(piece)] != piece:
                return False
        return True