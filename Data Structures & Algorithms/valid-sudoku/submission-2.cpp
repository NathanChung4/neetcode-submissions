class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // need 3 conditionals
        unordered_map<int, unordered_set<char>> rows;
        unordered_map<int, unordered_set<char>> cols;
        unordered_map<int, unordered_set<char>> squares;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }

                int square = ((r/3)*3 + (c/3));

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
