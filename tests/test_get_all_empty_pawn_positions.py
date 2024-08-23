from mill_game.game_boards.six_pawn_board import SixPawnBoard
from mill_game.player import Player


def test_get_all_empty_pawn_positions():
    player_a = Player("Jan Kowalski", "A")
    player_b = Player("Agnieszka Nowak", "B")
    initial_board = [[None],
                     [None, player_b, player_a, player_a,
                      player_a, None, None, None],
                     [None, None, None, None,
                      player_b, player_b, player_b, None]]
    game_board = SixPawnBoard(initial_board)
    assert game_board.get_all_empty_pawn_positions() == [(1, 0), (1, 5),
                                                         (1, 6), (1, 7),
                                                         (2, 0), (2, 1),
                                                         (2, 2), (2, 3),
                                                         (2, 7)]
