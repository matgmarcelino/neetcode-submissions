class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: dict[int, set[str]] = defaultdict(set)
        cols: dict[int, set[str]] = defaultdict(set)
        squares: dict[tuple, set[str]] = defaultdict(set)

        for r in range(9):
            for c in range(9):
                char: str = board[r][c]
                if char == '.':
                    continue

                if char in rows[r] or char in cols[c] or char in squares[r // 3, c // 3]:
                    return False
                
                rows[r].add(char)
                cols[c].add(char)
                squares[r // 3, c // 3].add(char)
        
        return True

