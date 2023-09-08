from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rule
        checklist = []
        for i in range(9):
            col_str = ""
            for j in range(9):
                col_str += board[j][i]

            checklist.append(col_str.replace('.', ''))

        # check rule 2
        for row in board:
            row_str = "".join(row).replace('.', '')
            checklist.append(row_str)  # fill row_str

        # check rule 3
        ''' (x9) x3 x3
        stop point
        22, 25, 28
        52, 55, 58
        82, 85, 88
        '''
        for i in range(3):
            box_str = ""
            i *= 3
            for j in range(9):
                box_str += board[i][j]   # 00, 01, 02
                box_str += board[i+1][j]  # 10, 11, 12
                box_str += board[i+2][j]  # 20, 21, 22
                if j % 3 == 2:
                    checklist.append(box_str.replace('.', ''))
                    box_str = ""

        # check
        for area in checklist:
            if len(area) != len(set(area)):
                return False
            else:
                pass

        return True

# best answer


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
