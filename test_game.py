import unittest
from game import Game


class TestGame(unittest.TestCase):

  def setUp(self):
    self.game = Game()
    self.board_size = 9

  def test_is_blank_in_top_row_true_1(self):
    blank_position = 1
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), True)

  def test_is_blank_in_top_row_true_2(self):
    blank_position = 2
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), True)

  def test_is_blank_in_top_row_true_3(self):
    blank_position = 3
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), True)

  def test_is_blank_in_top_row_false_4(self):
    blank_position = 4
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), False)

  def test_is_blank_in_top_row_false_5(self):
    blank_position = 5
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), False)

  def test_is_blank_in_top_row_false_6(self):
    blank_position = 6
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), False)

  def test_is_blank_in_top_row_false_7(self):
    blank_position = 7
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), False)

  def test_is_blank_in_top_row_false_8(self):
    blank_position = 8
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), False)

  def test_is_blank_in_top_row_false_9(self):
    blank_position = 9
    self.assertEqual(self.game.is_blank_in_top_row(blank_position, self.board_size), False)




  def test_is_blank_in_bottom_row_true_7(self):
    blank_position = 7
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), True)

  def test_is_blank_in_bottom_row_true_8(self):
    blank_position = 8
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), True)

  def test_is_blank_in_bottom_row_true_9(self):
    blank_position = 9
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), True)

  def test_is_blank_in_bottom_row_false_1(self):
    blank_position = 1
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), False)

  def test_is_blank_in_bottom_row_false_2(self):
    blank_position = 2
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), False)

  def test_is_blank_in_bottom_row_false_3(self):
    blank_position = 3
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), False)

  def test_is_blank_in_bottom_row_false_4(self):
    blank_position = 4
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), False)

  def test_is_blank_in_bottom_row_false_5(self):
    blank_position = 5
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), False)

  def test_is_blank_in_bottom_row_false_6(self):
    blank_position = 6
    self.assertEqual(self.game.is_blank_in_bottom_row(blank_position), False)


  def test_is_blank_in_left_column_true_1(self):
    blank_position = 1
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), True)

  def test_is_blank_in_left_column_false_2(self):
    blank_position = 2
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), False)

  def test_is_blank_in_left_column_false_3(self):
    blank_position = 3
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), False)

  def test_is_blank_in_left_column_true_4(self):
    blank_position = 4
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), True)

  def test_is_blank_in_left_column_false_5(self):
    blank_position = 5
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), False)

  def test_is_blank_in_left_column_false_6(self):
    blank_position = 6
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), False)

  def test_is_blank_in_left_column_true_7(self):
    blank_position = 7
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), True)

  def test_is_blank_in_left_column_false_8(self):
    blank_position = 8
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), False)

  def test_is_blank_in_left_column_false_9(self):
    blank_position = 9
    self.assertEqual(self.game.is_blank_in_left_column(blank_position), False)




  def test_is_blank_in_right_column_false_1(self):
    blank_position = 1
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), False)

  def test_is_blank_in_right_column_false_2(self):
    blank_position = 2
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), False)

  def test_is_blank_in_right_column_true_3(self):
    blank_position = 3
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), True)

  def test_is_blank_in_right_column_false_4(self):
    blank_position = 4
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), False)

  def test_is_blank_in_right_column_false_5(self):
    blank_position = 5
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), False)

  def test_is_blank_in_right_column_true_6(self):
    blank_position = 6
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), True)

  def test_is_blank_in_right_column_false_7(self):
    blank_position = 7
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), False)

  def test_is_blank_in_right_column_false_8(self):
    blank_position = 8
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), False)

  def test_is_blank_in_right_column_true_9(self):
    blank_position = 9
    self.assertEqual(self.game.is_blank_in_right_column(blank_position), True)


  def test_get_blank_neighbor_north_4(self):
    tiles = ["a", "b", "c",
             "  ", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 4)
    self.assertEqual(self.game.get_blank_neighbor_north(tiles), "a")

  def test_get_blank_neighbor_north_5(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 5)
    self.assertEqual(self.game.get_blank_neighbor_north(tiles), "b")

  def test_get_blank_neighbor_north_6(self):
    tiles = ["a", "b", "c",
             "d", "e", "  ",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 6)
    self.assertEqual(self.game.get_blank_neighbor_north(tiles), "c")

  def test_get_blank_neighbor_north_7(self):
    tiles = ["a", "b", "c",
             "d", "e", "f",
             "  ", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 7)
    self.assertEqual(self.game.get_blank_neighbor_north(tiles), "d")

  def test_get_blank_neighbor_north_8(self):
    tiles = ["a", "b", "c",
             "d", "e", "f",
             "g", "  ", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 8)
    self.assertEqual(self.game.get_blank_neighbor_north(tiles), "e")

  def test_get_blank_neighbor_north_9(self):
    tiles = ["a", "b", "c",
             "d", "e", "f",
             "g", "h", "  "]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 9)
    self.assertEqual(self.game.get_blank_neighbor_north(tiles), "f")

  def test_get_blank_neighbor_south_1(self):
    tiles = ["  ", "a", "b",
             "c", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 1)
    self.assertEqual(self.game.get_blank_neighbor_south(tiles), "c")

  def test_get_blank_neighbor_south_2(self):
    tiles = ["a", "  ", "b",
             "c", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 2)
    self.assertEqual(self.game.get_blank_neighbor_south(tiles), "d")

  def test_get_blank_neighbor_south_3(self):
    tiles = ["a", "b", "  ",
             "c", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 3)
    self.assertEqual(self.game.get_blank_neighbor_south(tiles), "e")

  def test_get_blank_neighbor_south_4(self):
    tiles = ["a", "b", "c",
             "  ", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 4)
    self.assertEqual(self.game.get_blank_neighbor_south(tiles), "f")

  def test_get_blank_neighbor_south_5(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 5)
    self.assertEqual(self.game.get_blank_neighbor_south(tiles), "g")

  def test_get_blank_neighbor_south_6(self):
    tiles = ["a", "b", "c",
             "d", "e", "  ",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 6)
    self.assertEqual(self.game.get_blank_neighbor_south(tiles), "h")

  def test_get_blank_neighbor_east_1(self):
    tiles = ["  ", "a", "b",
             "c", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 1)
    self.assertEqual(self.game.get_blank_neighbor_east(tiles), "a")

  def test_get_blank_neighbor_east_2(self):
    tiles = ["a", "  ", "b",
             "c", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 2)
    self.assertEqual(self.game.get_blank_neighbor_east(tiles), "b")

  def test_get_blank_neighbor_east_4(self):
    tiles = ["a", "b", "c",
             "  ", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 4)
    self.assertEqual(self.game.get_blank_neighbor_east(tiles), "d")

  def test_get_blank_neighbor_east_5(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 5)
    self.assertEqual(self.game.get_blank_neighbor_east(tiles), "e")

  def test_get_blank_neighbor_east_7(self):
    tiles = ["a", "b", "c",
             "d", "e", "f",
             "  ", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 7)
    self.assertEqual(self.game.get_blank_neighbor_east(tiles), "g")

  def test_get_blank_neighbor_east_8(self):
    tiles = ["a", "b", "c",
             "d", "e", "f",
             "g", "  ", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 8)
    self.assertEqual(self.game.get_blank_neighbor_east(tiles), "h")

  def test_get_blank_neighbor_west_3(self):
    tiles = ["a", "b", "  ",
             "c", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 3)
    self.assertEqual(self.game.get_blank_neighbor_west(tiles), "b")

  def test_get_blank_neighbor_west_2(self):
    tiles = ["a", "  ", "b",
             "c", "d", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 2)
    self.assertEqual(self.game.get_blank_neighbor_west(tiles), "a")

  def test_get_blank_neighbor_west_6(self):
    tiles = ["a", "b", "c",
             "d", "e", "  ",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 6)
    self.assertEqual(self.game.get_blank_neighbor_west(tiles), "e")

  def test_get_blank_neighbor_west_5(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 5)
    self.assertEqual(self.game.get_blank_neighbor_west(tiles), "d")

  def test_get_blank_neighbor_west_9(self):
    tiles = ["a", "b", "c",
             "d", "e", "f",
             "g", "h", "  "]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 9)
    self.assertEqual(self.game.get_blank_neighbor_west(tiles), "h")


  def test_get_blank_neighbor_west_8(self):
    tiles = ["a", "b", "c",
             "d", "e", "f",
             "g", "  ", "h"]
    blank_position = tiles.index("  ") + 1
    self.assertEqual(blank_position, 8)
    self.assertEqual(self.game.get_blank_neighbor_west(tiles), "g")

  def test_swap_up(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    target = "b"
    self.assertEqual(self.game.swap_tiles(tiles, target),
                     ["a", "  ", "c",
                      "d", "b", "e",
                      "f", "g", "h"])

  def test_swap_down(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    target = "g"
    self.assertEqual(self.game.swap_tiles(tiles, target),
                     ["a", "b", "c",
                      "d", "g", "e",
                      "f", "  ", "h"])

  def test_swap_left(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    target = "d"
    self.assertEqual(self.game.swap_tiles(tiles, target),
                     ["a", "b", "c",
                      "  ", "d", "e",
                      "f", "g", "h"])

  def test_swap_right(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    target = "e"
    self.assertEqual(self.game.swap_tiles(tiles, target),
                     ["a", "b", "c",
                      "d", "e", "  ",
                      "f", "g", "h"])

  def test_make_move_right(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    self.assertEqual(self.game.make_move_right(tiles),
                     ["a", "b", "c",
                      "  ", "d", "e",
                      "f", "g", "h"])

  def test_make_move_left(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    self.assertEqual(self.game.make_move_left(tiles),
                     ["a", "b", "c",
                      "d", "e", "  ",
                      "f", "g", "h"])

  def test_make_move_up(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    self.assertEqual(self.game.make_move_up(tiles),
                     ["a", "b", "c",
                      "d", "g", "e",
                      "f", "  ", "h"])

  def test_make_move_down(self):
    tiles = ["a", "b", "c",
             "d", "  ", "e",
             "f", "g", "h"]
    self.assertEqual(self.game.make_move_down(tiles),
                     ["a", "  ", "c",
                      "d", "b", "e",
                      "f", "g", "h"])


  def test_make_move(self):
      tiles = ["a", "b", "c",
               "d", "  ", "e",
               "f", "g", "h"]
      self.assertEqual(self.game.make_move(tiles, "right"),
                       ["a", "b", "c",
                        "  ", "d", "e",
                        "f", "g", "h"])
