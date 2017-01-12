import random

class Game(object):

    def __init__(self, board_presenter, cli, dimensions):
        self.board_presenter = board_presenter
        self.cli = cli
        self.rows = dimensions['rows']
        self.cols = dimensions['cols']

    def play_game(self):
        tiles = self.create_tile_list()
        self.display_current_board(tiles)
        interpreted_input = self.take_a_turn(tiles)
        while (interpreted_input != "exit"):
            interpreted_input = self.take_a_turn(tiles)
            if self.is_a_won_game(tiles):
                self.cli.display("You win!")

    def create_tile_list(self):
        tiles = []
        for i in range(self.rows * self.cols):
            if (i + 1) < 10:
                tiles.append(" " + str(i + 1))
            else:
                tiles.append(str(i + 1))
        tiles[len(tiles) - 1] = "  "
        return tiles

    def display_current_board(self, tiles):
        self.cli.clear_screen()
        self.cli.display_legend()
        self.board_presenter.print_board(tiles, self.rows, self.cols)

    def take_a_turn(self, tiles):
        interpreted_input = self.get_interpreted_input()
        tiles = self.make_move(tiles, interpreted_input)
        self.display_current_board(tiles)
        return interpreted_input

    def get_interpreted_input(self):
        user_input = self.cli.get_input()
        return self.interpret_input(user_input)

    def is_a_won_game(self, tiles):
        return tiles == self.create_tile_list()

    def interpret_input(self, user_input):
        if user_input == "i":
            return "up"
        elif user_input == "j":
            return "left"
        elif user_input == "k":
            return "down"
        elif user_input == "l":
            return "right"
        elif user_input == "s":
            return "shuffle"
        elif user_input == "e":
            return "exit"
        else:
            return user_input

    def get_blank_position(self, tiles):
        return tiles.index("  ") + 1

    def is_blank_in_top_row(self, blank_position, boardlength):
        return blank_position <= self.cols

    def is_blank_in_bottom_row(self, blank_position):
        return self.rows * self.cols - blank_position < self.cols

    def is_blank_in_left_column(self, blank_position):
        return blank_position % self.cols == 1

    def is_blank_in_right_column(self, blank_position):
        return blank_position % self.cols == 0

    def is_valid_move(self, tiles, move):
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


    def swap_tiles(self, tiles, swap_target):
       temp_value_target = tiles.index(swap_target)
       temp_value_blank = tiles.index("  ")
       tiles[temp_value_target] = "  "
       tiles[temp_value_blank] = swap_target
       return tiles


    def get_blank_neighbor_north(self, tiles):
        return tiles[self.get_blank_position(tiles) - self.cols - 1]

    def get_blank_neighbor_south(self, tiles):
        return tiles[self.get_blank_position(tiles) + self.cols - 1]

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
        elif move == "down":
            return self.make_move_down(tiles)
        elif move == "shuffle":
            return self.shuffle_tiles(tiles)
        else:
            return tiles


    def shuffle_tiles(self, tiles):
        moves = ["up", "down", "left", "right"]
        for i in range(1, 50*len(tiles)):
            move = random.choice(moves)
            self.make_move(tiles, move)
        return tiles
