import random

class SudokuBoard:

    def __init__(self):
        self.board = []
        for i in range(9): 
            row = [0] * 9 
            self.board.append(row)
        self.generate_board()


    def __str__(self):
        rows = [] 
        for row in range(9):
            row_str = "" 
            for col in range(9):
                num_str = str(self.board[row][col])
                row_str += num_str + " "
                if col == 2 or col == 5:
                    row_str += "| "
            rows.append(row_str.strip())
            if row == 2 or row == 5:
                rows.append("- " * 11)
        return "\n".join(rows)
    
    def generate_board(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col] = random.randint(1, 9)
    
    def check_row(self, row_num):
        row = self.board[row_num]
        duplicate = set()
        for num in row:
            if num == 0:
                continue
            if num in duplicate:
                return False
            duplicate.add(num)
        return True
    
    def check_col(self, col_num):
        col = []
        for row_num in range(9):
            col.append(self.board[row_num][col_num])
        duplicate = set()
        for num in col:
            if num == 0:
                continue
            if num in duplicate:
                return False
            duplicate.add(num)
        return True


sudoku_board = SudokuBoard()

print("Sudoku board: ")
print(sudoku_board)

all_rows_correct = True
for row_num in range(9):
    if not sudoku_board.check_row(row_num):
        all_rows_correct = False
        break

all_cols_correct = True
for col_num in range(9):
    if not sudoku_board.check_col(col_num):
        all_cols_correct = False
        break

if all_rows_correct:
    print("All rows are correct")
else:
    print("At least one row is incorrect")

if all_cols_correct:
    print("All columns are correct")
else:
    print("At least one column is incorrect")