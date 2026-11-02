class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])

        top: int = 0
        bot: int = ROWS - 1
        while top <= bot:
            row: int = (top + bot) // 2

            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break

        row: int = (top + bot) // 2

        l: int = 0
        r: int = COLS - 1
        while l <= r:
            m: int = (l + r) // 2

            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False







