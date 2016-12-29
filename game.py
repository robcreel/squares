from board_presenter import BoardPresenter
import config

# rows = config.ROWS
# cols = config.COLS
rows = 3
cols = 3
# tiles = ["a", "b", "c", "d", "  ", "e", "f", "g", "h"]



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

    def get_blank_position(self, tiles):
        return tiles.index("  ") + 1

    def is_blank_in_top_row(self, blank_position, boardlength):
        # print(len(tiles))
        # print(blank_position)
        # print(cols)
        return blank_position <= cols

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
            return not(self.is_blank_in_top_row(blank_position, len(tiles)))
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
    def get_blank_neighbor_north(self, tiles):
        return tiles[self.get_blank_position(tiles) - cols - 1]

    def get_blank_neighbor_south(self, tiles):
        return tiles[self.get_blank_position(tiles) + cols - 1]

    def get_blank_neighbor_east(self, tiles):
        return tiles[self.get_blank_position(tiles)]

    def get_blank_neighbor_west(self, tiles):
        return tiles[self.get_blank_position(tiles) - 2]

# game = Game()
# print("blank_position: {0}".format(blank_position))
# print("North: {0}".format(game.get_blank_neighbor_north()))
# print("South: {0}".format(game.get_blank_neighbor_south()))
# print("East: {0}".format(game.get_blank_neighbor_east()))
# print("West: {0}".format(game.get_blank_neighbor_west()))
