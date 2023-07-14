class Solution(object):
    def isValidSudoku(self, board):
        def is_valid_unit(unit):
            seen = set()
            for digit in unit:
                if digit != "." and digit in seen:
                    return False
                seen.add(digit)
            return True

        # Check rows
        for row in board:
            if not is_valid_unit(row):
                return False

        # Check columns
        for col in zip(*board):
            if not is_valid_unit(col):
                return False

        # Check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [
                    board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)
                ]
                if not is_valid_unit(sub_box):
                    return False

        return True

        """
        :type board: List[List[str]]
        :rtype: bool
        """