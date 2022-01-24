from game_boards.six_pawn_board import SixPawnBoard
from player import Player


def test_get_all_empty_pawn_positions():
    playerA = Player("Jan Kowalski", "A")
    playerB = Player("Agnieszka Nowak", "B")
    initial_board = [[None],
                     [None, playerB, playerA, playerA, playerA, None, None, None],
                     [None, None, None, None, playerB, playerB, playerB, None]]
    game_board = SixPawnBoard(initial_board)
    assert game_board.get_all_empty_pawn_positions() == [(1, 0), (1, 5), (1, 6),
                                                         (1, 7), (2, 0), (2, 1),
                                                         (2, 2), (2, 3), (2, 7)]
