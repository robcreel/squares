import random

rows = 2
cols = 2


class Game(object):

    def __init__(self, board_presenter):
        self.board_presenter = board_presenter

    def play_game(self):
        tiles = self.create_tile_list()
        self.board_presenter.print_board(tiles, rows, cols)

    # Method for determining win/game over status, 
    # create while loop that doesn't terminate until gameover = true
    # print board after game.

    def create_tile_list(self):
        tiles = []
        for i in range(rows * cols):
            if (i + 1) < 10:
                tiles.append(" " + str(i + 1))
            else:
                tiles.append(str(i + 1))
        tiles[len(tiles) - 1] = "  "
        return tiles

    def get_blank_position(self, tiles):
        return tiles.index("  ") + 1

    def is_blank_in_top_row(self, blank_position, boardlength):
        return blank_position <= cols

    def is_blank_in_bottom_row(self, blank_position):
        return rows*cols - blank_position < cols

    def is_blank_in_left_column(self, blank_position):
        return blank_position % cols == 1

    def is_blank_in_right_column(self, blank_position):
        return blank_position % cols == 0

    def is_valid_move(self, tiles, move):
        presenter = BoardPresenter()
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


    def swap_tiles(self, tiles, swap_target): # swap_target is a tile value
       temp_value_target = tiles.index(swap_target)
       temp_value_blank = tiles.index("  ")
       tiles[temp_value_target] = "  "
       tiles[temp_value_blank] = swap_target
       return tiles


    def get_blank_neighbor_north(self, tiles):
        return tiles[self.get_blank_position(tiles) - cols - 1]

    def get_blank_neighbor_south(self, tiles):
        return tiles[self.get_blank_position(tiles) + cols - 1]

    def get_blank_neighbor_east(self, tiles):
        return tiles[self.get_blank_position(tiles)]

    def get_blank_neighbor_west(self, tiles):
        return tiles[self.get_blank_position(tiles) - 2]

    def make_move_right(self, tiles):
        if self.is_valid_move(tiles, "right"):
            self.swap_tiles(tiles, self.get_blank_neighbor_west(tiles))
        return tiles

    def make_move_left(self, tiles):
        if self.is_valid_move(tiles, "left"):
            self.swap_tiles(tiles, self.get_blank_neighbor_east(tiles))
        return tiles

    def make_move_up(self, tiles):
        if self.is_valid_move(tiles, "up"):
            self.swap_tiles(tiles, self.get_blank_neighbor_south(tiles))
        return tiles

    def make_move_down(self, tiles):
        if self.is_valid_move(tiles, "down"):
            self.swap_tiles(tiles, self.get_blank_neighbor_north(tiles))
        return tiles

    def make_move(self, tiles, move):
        if move == "left":
            return self.make_move_left(tiles)
        elif move == "right":
            return self.make_move_right(tiles)
        elif move == "up":
            return self.make_move_up(tiles)
        else:
            return self.make_move_down(tiles)


    def shuffle_tiles(self, tiles):
        moves = ["up", "down", "left", "right"]
        for i in range(1, 4*len(tiles)):
            index = random.randint(0, 3)
            move = moves[index]
            self.make_move(tiles, move)
        print(tiles)
        return tiles
