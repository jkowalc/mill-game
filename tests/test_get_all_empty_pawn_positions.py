from mill_game.game_boards.six_pawn_board import SixPawnBoard
from mill_game.player import PlayerSymbol


def test_get_all_empty_pawn_positions():
    initial_board = [[None],
                     [None, PlayerSymbol.B, PlayerSymbol.A, PlayerSymbol.A,
                      PlayerSymbol.A, None, None, None],
                     [None, None, None, None,
                      PlayerSymbol.B, PlayerSymbol.B, PlayerSymbol.B, None]]
    game_board = SixPawnBoard(initial_board)
    assert game_board.get_all_empty_pawn_positions() == [(1, 0), (1, 5),
                                                         (1, 6), (1, 7),
                                                         (2, 0), (2, 1),
                                                         (2, 2), (2, 3),
                                                         (2, 7)]
