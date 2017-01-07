from game import Game
from board_presenter import BoardPresenter

# initialize each class.
board_presenter = BoardPresenter()
game = Game(board_presenter)

game.play_game()



#dependency injection
