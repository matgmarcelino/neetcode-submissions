class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: dict[int, set] = defaultdict(set)
        cols: dict[int, set] = defaultdict(set)
        squares: dict[tuple, set] = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue

                num: int = int(board[r][c])
                if num in rows[r] or num in cols[c] or num in squares[r // 3, c // 3]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                squares[r // 3, c // 3].add(num)
        
        return True