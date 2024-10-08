from mill_game.game_boards.six_pawn_board import SixPawnBoard
from mill_game.game_boards.nine_pawn_board import NinePawnBoard
from mill_game.game_boards.twelve_pawn_board import TwelvePawnBoard
from mill_game.player import PlayerColor


def test_check_if_pawn_in_mill_sides():
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
        [None, None, None, None, None, None, None, None],
    ]
    game_board = NinePawnBoard(initial_board)

    # player A
    assert game_board.check_if_pawn_in_mill((1, 2))
    assert game_board.check_if_pawn_in_mill((1, 3))
    assert game_board.check_if_pawn_in_mill((1, 4))

    # player B
    assert game_board.check_if_pawn_in_mill((2, 4))
    assert game_board.check_if_pawn_in_mill((2, 5))
    assert game_board.check_if_pawn_in_mill((2, 6))

    assert not game_board.check_if_pawn_in_mill((1, 1))


def test_check_if_pawn_in_mill_sides_6_pawns():
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

    # player A
    assert game_board.check_if_pawn_in_mill((1, 2))
    assert game_board.check_if_pawn_in_mill((1, 3))
    assert game_board.check_if_pawn_in_mill((1, 4))

    # player B
    assert game_board.check_if_pawn_in_mill((2, 4))
    assert game_board.check_if_pawn_in_mill((2, 5))
    assert game_board.check_if_pawn_in_mill((2, 6))

    assert not game_board.check_if_pawn_in_mill((1, 1))


def test_check_if_pawn_in_mill_diagonals_12_pawns():
    initial_board = [
        [None],
        [None, None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None],
        [None, None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None],
        [None, None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None],
    ]
    game_board = TwelvePawnBoard(initial_board)

    assert game_board.check_if_pawn_in_mill((1, 2))
    assert game_board.check_if_pawn_in_mill((2, 2))
    assert game_board.check_if_pawn_in_mill((3, 2))

    assert game_board.check_if_pawn_in_mill((1, 4))
    assert game_board.check_if_pawn_in_mill((2, 4))
    assert game_board.check_if_pawn_in_mill((3, 4))

    assert not game_board.check_if_pawn_in_mill((1, 7))


def test_check_if_pawn_in_mill_diagonals_9_pawns():
    initial_board = [
        [None],
        [None, None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None],
        [None, None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None],
        [None, None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None],
    ]
    game_board = NinePawnBoard(initial_board)

    assert not game_board.check_if_pawn_in_mill((1, 2))
    assert not game_board.check_if_pawn_in_mill((2, 2))
    assert not game_board.check_if_pawn_in_mill((3, 2))

    assert not game_board.check_if_pawn_in_mill((1, 4))
    assert not game_board.check_if_pawn_in_mill((2, 4))
    assert not game_board.check_if_pawn_in_mill((3, 4))

    assert not game_board.check_if_pawn_in_mill((1, 7))


def test_check_if_pawn_in_mill_diff_rectangle_12_pawns():
    initial_board = [
        [None],
        [None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None, None],
        [None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None, None],
        [
            None,
            PlayerColor.WHITE,
            None,
            PlayerColor.BLACK,
            None,
            PlayerColor.BLACK,
            None,
            None,
        ],
    ]
    game_board = TwelvePawnBoard(initial_board)

    assert game_board.check_if_pawn_in_mill((1, 1))
    assert game_board.check_if_pawn_in_mill((2, 1))
    assert game_board.check_if_pawn_in_mill((3, 1))
    assert game_board.check_if_pawn_in_mill((1, 3))
    assert game_board.check_if_pawn_in_mill((2, 3))
    assert game_board.check_if_pawn_in_mill((3, 3))
    assert not game_board.check_if_pawn_in_mill((3, 5))


def test_check_if_pawn_in_mill_diff_rectangle_9_pawns():
    initial_board = [
        [None],
        [None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None, None],
        [None, PlayerColor.WHITE, None, PlayerColor.BLACK, None, None, None, None],
        [
            None,
            PlayerColor.WHITE,
            None,
            PlayerColor.BLACK,
            None,
            PlayerColor.BLACK,
            None,
            None,
        ],
    ]
    game_board = NinePawnBoard(initial_board)

    assert game_board.check_if_pawn_in_mill((1, 1))
    assert game_board.check_if_pawn_in_mill((2, 1))
    assert game_board.check_if_pawn_in_mill((3, 1))

    assert game_board.check_if_pawn_in_mill((1, 3))
    assert game_board.check_if_pawn_in_mill((2, 3))
    assert game_board.check_if_pawn_in_mill((3, 3))

    assert not game_board.check_if_pawn_in_mill((3, 5))
