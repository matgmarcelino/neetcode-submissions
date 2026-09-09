class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new HashSet[9];
        Set<Character>[] cols = new HashSet[9];
        Set<Character>[] sqrs = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            sqrs[i] = new HashSet<>();
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char sqr = board[i][j];
                if (sqr == '.') continue;

                int sqrIdx = (i / 3) * 3 + (j / 3);
                if (!rows[i].add(sqr) || !cols[j].add(sqr) || !sqrs[sqrIdx].add(sqr)) 
                    return false;
            }
        }

        return true;
    }
}
