class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS: int = len(matrix)
        COLS: int = len(matrix[0])

        top: int = 0
        bot: int = ROWS - 1
        while top <= bot:
            row: int = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False

        l: int = 0
        r: int = COLS - 1
        row: int = (top + bot) // 2

        while l <= r:
            m: int = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False

                