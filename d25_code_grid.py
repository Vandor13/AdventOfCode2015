TARGET_ROW = 2981
TARGET_COLUMN = 3075
MULTIPLICATOR = 252533
MODULO = 33554393

class CodeGrid:
    def __init__(self):
        self.first_code = 20151125
        self.row = 1
        self.column = 1
        self.current_code = self.first_code

    def calculate_next_code(self):
        next_code = (self.current_code * MULTIPLICATOR) % MODULO
        if self.row == 1:
            self.row = self.column + 1
            self.column = 1
            if self.row % 100 == 0:
                print("Row", self.row)
        else:
            self.row -= 1
            self.column += 1
        self.current_code = next_code
        # print(f"Row {self.row} Column {self.column}: {self.current_code}")


    def do_n_calculations(self, n):
        for i in range(n):
            self.calculate_next_code()

    def find_value(self, row, column):
        while True:
            if self.row == row and self.column == column:
                print("Found value:", self.current_code)
                break
            else:
                self.calculate_next_code()


grid = CodeGrid()
# grid.do_n_calculations(10)
grid.find_value(TARGET_ROW, TARGET_COLUMN)
