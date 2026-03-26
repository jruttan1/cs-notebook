class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # every board is exactly 9x9
        # you can do integer division to figure out your box, row // 3 & column // 3 gives you the index of the box
        # flatted 2d to 1d to index box: row * cols + col = i//3 * 3 + j//3 gives corresponding index from 0-8

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
 
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in boxes[i//3 * 3 + j//3]:
                    return False
                elif board[i][j] != ".":
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    boxes[i//3 * 3 + j//3].add(board[i][j])

        return True

# Very unintuitize for me, definitely need to practice grid problems more and redo this one eventually