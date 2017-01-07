class BoardPresenter(object):

    def print_row(self, tiles, first, last): # Prints row of tiles from first to last
        row = "|"
        for index in range(first, last):
            row += " " + str(tiles[index - 1]) + " |"
        print(row)

    def print_row_border(self, first, last): # Prints row border of length last - first
        row_border = ""
        for index in range(first, last):
            row_border += "-----"
        row_border += "-"
        print(row_border)

    def print_board(self, tiles, nrows, ncols):
        for index in range(1, ncols * nrows + 1, ncols):
            self.print_row_border(index, index + ncols)
            self.print_row(tiles, index, index + ncols)
        self.print_row_border(0, ncols)
