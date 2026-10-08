class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if (top > bot):
            return False
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        while (l <= r):
            c = (l + r) // 2
            num = matrix[row][c]

            if num > target:
                r = c - 1
            elif num < target:
                l = c + 1
            else:
                return True

        return False
