from game import Game
from board_presenter import BoardPresenter
from cli import CLI
from setup import Setup

board_presenter = BoardPresenter()
cli = CLI()
setup = Setup(cli)
dimensions = setup.get_dimensions()
game = Game(board_presenter, cli, dimensions)

game.play_game()
