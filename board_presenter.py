import config

rows = config.ROWS
cols = config.COLS

class BoardPresenter(object):

    def printRow(self, tiles, first, last): # Prints row of tiles from first to last
        row = "|"
        for index in range(first, last):
            row += " " + str(tiles[index - 1]) + " |"
        print(row)


    def printRowBorder(self, first, last): # Prints row border of length last - first
        rowBorder = ""
        for index in range(first, last):
            rowBorder += "-----"
        rowBorder += "-"
        print(rowBorder)

    def printBoard(self, nrows, ncols):
        tiles = self.createTileList()
        for index in range(1, ncols * nrows + 1, ncols):
            self.printRowBorder(index, index + ncols)
            self.printRow(tiles, index, index + ncols)
        self.printRowBorder(0, ncols)

    def createTileList(self):
        tiles = []
        for i in range(rows * cols):
            if (i + 1) < 10:
                tiles.append(" " + str(i + 1))
            else:
                tiles.append(str(i + 1))
        tiles[len(tiles) - 1] = "  "
        return tiles

presenter = BoardPresenter()
presenter.printBoard(rows, cols)
