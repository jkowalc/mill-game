from mill_game.game_boards.six_pawn_board import SixPawnBoard
from mill_game.player import PlayerColor


def test_get_all_empty_pawn_positions():
    initial_board = [
        [None],
        [
            None,
            PlayerColor.BLACK,
            PlayerColor.WHITE,
            PlayerColor.WHITE,
            PlayerColor.WHITE,
            None,
            None,
            None,
        ],
        [
            None,
            None,
            None,
            None,
            PlayerColor.BLACK,
            PlayerColor.BLACK,
            PlayerColor.BLACK,
            None,
        ],
    ]
    game_board = SixPawnBoard(initial_board)
    assert game_board.get_all_empty_pawn_positions() == [
        (1, 0),
        (1, 5),
        (1, 6),
        (1, 7),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 7),
    ]
