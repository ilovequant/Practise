class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """

    def isValidSudoku(self, board):
        # write your code here
        m = len(board)
        n = len(board[0])

        rowset = [set() for i in range(m)]
        colset = [set() for j in range(n)]
        blockset = [set() for k in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rowset[i] or board[i][j] in colset[j] or board[i][j] in blockset[i // 3 * 3 + j // 3]:
                    return False

                rowset[i].add(board[i][j])
                colset[j].add(board[i][j])
                blockset[i // 3 * 3 + j // 3].add(board[i][j])

        return True