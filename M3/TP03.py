# L'échequier de Sissa

# Definition of cells of a chess board
class Cell:
    def __init__(self, row, column, row_name, col_name, id):
        self.row = row
        self.column = column
        self.row_name = row_name
        self.col_name = col_name
        self.name = ""
        self.id = id
        self.nb_seeds = 0

    def get_id(self):
        return self.id

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def set_name(self):
        self.name = self.col_name + self.row_name

# Definition of a chess board
class ChessBoard:
    def __init__(self, nb_row, nb_col, row_names, col_names):
        self.nb_row = nb_row
        self.nb_col = nb_col
        self.row_names = row_names
        self.col_names = col_names
        self.cells = []
        self.cells_by_id = {}

    def create_cells(self):
        k = 0
        for i in range(0, self.nb_row):
            for j in range(0, self.nb_col):
                current_cell = Cell(i, j, self.row_names[i], self.col_names[j], k)
                self.cells.append(current_cell)
                self.cells_by_id[k] = current_cell
                k += 1
        print(str(len(self.cells)) + " cells created")

    def print_col_names(self):
        col_names_row = " "
        for i in range(0, len(self.col_names)):
            col_names_row += "  " + self.col_names[i] + " "
        print(col_names_row)

    def print_chess_board(self):
        self.print_col_names()
        for i in range(self.nb_row - 1, -1, -1):
            row1 = "  "
            row2 = " "
            row3 = "  "
            if i == 0:
                for j in range(0, self.nb_col):
                    row1 += "————"
                print(row1)
            for j in range(0, self.nb_col):
                if j == 0:
                    row2 += self.row_names[i]
                row2 += "|  |"
            print(row2)
            for j in range(0, self.nb_col):
                row3 += "————"
            print(row3)
        self.print_col_names()

    def calcule_nb_seeds(self):
        total = 1
        k = 0

        for i in range(1, self.nb_row + 1):
            for j in range(1, self.nb_col + 1):
                print(total)

                total = total * 2
                k += 1
        print(str(k) + " seeds calculated")

chess_board = ChessBoard(
    8,
    8,
    ["1", "2", "3", "4", "5", "6", "7", "8"],
    ["A", "B", "C", "D", "E", "F", "G", "H"]
)

chess_board.create_cells()
chess_board.print_chess_board()
chess_board.calcule_nb_seeds()