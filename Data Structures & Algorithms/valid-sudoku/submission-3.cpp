class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<int, unordered_set<int>> rows;
        map<int, unordered_set<int>> cols;
        map<int, unordered_set<int>> squares;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                int square = (r/3) * 3 + (c/3);

                if (rows[r].count(board[r][c]) || cols[c].count(board[r][c]) || squares[square].count(board[r][c])) {
                    return false;
                }
                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                squares[square].insert(board[r][c]);

            }
        }
        return true;

    }
};
