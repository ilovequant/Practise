class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """

    def solveSudoku(self, board):
        # write your code here
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        square = [set() for i in range(9)]
        res = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    res.append([i, j])
                    continue

                row[i].add(board[i][j])
                col[j].add(board[i][j])
                square[3 * (i / 3) + j / 3].add(board[i][j])

        self.helper(0, res, row, col, square, board)
        return board

    def helper(self, index, tofill, row, col, square, board):
        if index == len(tofill):
            return True

        l = tofill[index][0]
        r = tofill[index][1]
        for temp in range(1, 10):
            if temp not in row[l] and temp not in col[r] and temp not in square[3 * (l / 3) + (r / 3)]:
                board[l][r] = temp
                row[l].add(temp)
                col[r].add(temp)
                square[3 * (l / 3) + (r / 3)].add(temp)
                if self.helper(index + 1, tofill, row, col, square, board):
                    return True
                board[l][r] = 0
                row[l].remove(temp)
                col[r].remove(temp)
                square[3 * (l / 3) + (r / 3)].remove(temp)

        return False