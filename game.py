from board_presenter import BoardPresenter
import config

# rows = config.ROWS
# cols = config.COLS
rows = 3
cols = 3
tiles = ["a", "b", "c", "d", "  ", "e", "f", "g", "h"]
blank_position = tiles.index("  ") + 1


class Game(object):
    # Goal: decide on (and implement) the logic of tile movement.
    # isValid method:  up is valid if blank is not in last row, namely
    #   len(tiles) - blank.location < cols
    # down is valid if blank is not in the first row, namely
    #   blank.location < cols
    # left is valid if blank is not in the leftmost column, namely
    #   blank.location % cols != 1
    # right is valid if blank is not in the rightmost column, namely
    #   blank.location % cols != 0

    def is_blank_in_top_row(self, blank_position, tiles):
        # print(len(tiles))
        # print(blank_position)
        # print(cols)
        return len(tiles) - blank_position >= cols

    def is_blank_in_bottom_row(self, blank_position):
        return rows*cols - blank_position < cols

    def is_blank_in_left_column(self, blank_position):
        return blank_position % cols == 1

    def is_blank_in_right_column(self, blank_position):
        return blank_position % cols == 0

    def is_valid_move(self, move):
        presenter = BoardPresenter()
        # tiles = presenter.createTileList()
        # tiles = ["a", "b", "c", "d", "  ", "e", "f", "g", "h"]

        blank_position = tiles.index("  ") + 1
        if move == "down":
            return not(self.is_blank_in_top_row(blank_position, tiles))
        elif move == "up":
            return not(self.is_blank_in_bottom_row(blank_position))
        elif move == "left":
            return not(self.is_blank_in_right_column(blank_position))
        elif move == "right":
            return not(self.is_blank_in_left_column(blank_position))
        else:
            return False



    # def moveTile(move):
    #     if isValidMove(move):
    #         if move = up:
    #             swap(blank, )
    #         elif move = down:
    #
    #         elif move = left:
    #
    #         elif move = right:
    #
    #
    def getBlankNeighborNorth(self, blank_position):
        return tiles[blank_position - cols - 1]

    def getBlankNeighborSouth(self, blank_position):
        return tiles[blank_position + cols]

    def getBlankNeighborEast(self, blank_position):
        return tiles[blank_position]

    def getBlankNeighborWest(self, blank_position):
        return tiles[blank_position - 2]

game = Game()
print("blank_position: {0}".format(blank_position))
print("North: {0}".format(game.getBlankNeighborNorth(blank_position)))
print("South: {0}".format(game.getBlankNeighborSouth(blank_position)))
print("East: {0}".format(game.getBlankNeighborEast(blank_position)))
print("West: {0}".format(game.getBlankNeighborWest(blank_position)))
