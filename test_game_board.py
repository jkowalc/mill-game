from mimetypes import init
from game_board import GameBoard
from player import Player


def test_check_if_pawn_in_mill_sides():
    playerA = Player("Jan Kowalski")
    playerB = Player("Agnieszka Nowak")
    initial_board = [[None],
                     [None, playerB, playerA, playerA, playerA, None, None, None],
                     [None, None, None, None, playerB, playerB, playerB, None],
                     [None, None, None, None, None, None, None, None]]
    game_board = GameBoard(3, False, False, initial_board)

    # playerA
    assert game_board.check_if_pawn_in_mill((1, 2)) == [(1, 2), (1, 3), (1, 4)]
    assert game_board.check_if_pawn_in_mill((1, 3)) == [(1, 2), (1, 3), (1, 4)]
    assert game_board.check_if_pawn_in_mill((1, 4)) == [(1, 2), (1, 3), (1, 4)]

    # player B
    assert game_board.check_if_pawn_in_mill((2, 4)) == [(2, 4), (2, 5), (2, 6)]
    assert game_board.check_if_pawn_in_mill((2, 5)) == [(2, 4), (2, 5), (2, 6)]
    assert game_board.check_if_pawn_in_mill((2, 6)) == [(2, 4), (2, 5), (2, 6)]

    assert game_board.check_if_pawn_in_mill((1, 1)) is None


def test_check_if_pawn_in_mill_sides_6_pawns():
    playerA = Player("Jan Kowalski")
    playerB = Player("Agnieszka Nowak")
    initial_board = [[None],
                     [None, playerB, playerA, playerA, playerA, None, None, None],
                     [None, None, None, None, playerB, playerB, playerB, None]]
    game_board = GameBoard(2, False, False, initial_board)

    # playerA
    assert game_board.check_if_pawn_in_mill((1, 2)) == [(1, 2), (1, 3), (1, 4)]
    assert game_board.check_if_pawn_in_mill((1, 3)) == [(1, 2), (1, 3), (1, 4)]
    assert game_board.check_if_pawn_in_mill((1, 4)) == [(1, 2), (1, 3), (1, 4)]

    # player B
    assert game_board.check_if_pawn_in_mill((2, 4)) == [(2, 4), (2, 5), (2, 6)]
    assert game_board.check_if_pawn_in_mill((2, 5)) == [(2, 4), (2, 5), (2, 6)]
    assert game_board.check_if_pawn_in_mill((2, 6)) == [(2, 4), (2, 5), (2, 6)]

    assert game_board.check_if_pawn_in_mill((1, 1)) is None

def test_check_if_pawn_in_mill_diagonals_12_pawns():
    playerA = Player("Jan Kowalski")
    playerB = Player("Agnieszka Nowak")
    initial_board = [[None],
                     [None, None, playerA, None, playerB, None, None, None],
                     [None, None, playerA, None, playerB, None, None, None],
                     [None, None, playerA, None, playerB, None, None, None]]
    game_board = GameBoard(3, True, False, initial_board)

    assert game_board.check_if_pawn_in_mill((1, 2)) == [(1, 2), (2, 2), (3, 2)]
    assert game_board.check_if_pawn_in_mill((2, 2)) == [(1, 2), (2, 2), (3, 2)]
    assert game_board.check_if_pawn_in_mill((3, 2)) == [(1, 2), (2, 2), (3, 2)]

    assert game_board.check_if_pawn_in_mill((1, 4)) == [(1, 4), (2, 4), (3, 4)]
    assert game_board.check_if_pawn_in_mill((2, 4)) == [(1, 4), (2, 4), (3, 4)]
    assert game_board.check_if_pawn_in_mill((3, 4)) == [(1, 4), (2, 4), (3, 4)]

    assert game_board.check_if_pawn_in_mill((1, 7)) is None


def test_check_if_pawn_in_mill_diagonals_9_pawns():
    playerA = Player("Jan Kowalski")
    playerB = Player("Agnieszka Nowak")
    initial_board = [[None],
                     [None, None, playerA, None, playerB, None, None, None],
                     [None, None, playerA, None, playerB, None, None, None],
                     [None, None, playerA, None, playerB, None, None, None]]
    game_board = GameBoard(3, False, False, initial_board)

    assert game_board.check_if_pawn_in_mill((1, 2)) is None
    assert game_board.check_if_pawn_in_mill((2, 2)) is None
    assert game_board.check_if_pawn_in_mill((3, 2)) is None

    assert game_board.check_if_pawn_in_mill((1, 4)) is None
    assert game_board.check_if_pawn_in_mill((2, 4)) is None
    assert game_board.check_if_pawn_in_mill((3, 4)) is None

    assert game_board.check_if_pawn_in_mill((1, 7)) is None


def test_check_if_pawn_in_mill_diff_rectangle_12_pawns():
    playerA = Player("Jan Kowalski")
    playerB = Player("Agnieszka Nowak")
    initial_board = [[None],
                     [None, playerA, None, playerB, None, None, None, None],
                     [None, playerA, None, playerB, None, None, None, None],
                     [None, playerA, None, playerB, None, playerB, None, None]]
    game_board = GameBoard(3, True, False, initial_board)

    assert game_board.check_if_pawn_in_mill((1, 1)) == [(1, 1), (2, 1), (3, 1)]
    assert game_board.check_if_pawn_in_mill((2, 1)) == [(1, 1), (2, 1), (3, 1)]
    assert game_board.check_if_pawn_in_mill((3, 1)) == [(1, 1), (2, 1), (3, 1)]

    assert game_board.check_if_pawn_in_mill((1, 3)) == [(1, 3), (2, 3), (3, 3)]
    assert game_board.check_if_pawn_in_mill((2, 3)) == [(1, 3), (2, 3), (3, 3)]
    assert game_board.check_if_pawn_in_mill((3, 3)) == [(1, 3), (2, 3), (3, 3)]

    assert game_board.check_if_pawn_in_mill((3, 5)) is None


def test_check_if_pawn_in_mill_diff_rectangle_9_pawns():
    playerA = Player("Jan Kowalski")
    playerB = Player("Agnieszka Nowak")
    initial_board = [[None],
                     [None, playerA, None, playerB, None, None, None, None],
                     [None, playerA, None, playerB, None, None, None, None],
                     [None, playerA, None, playerB, None, playerB, None, None]]
    game_board = GameBoard(3, False, False, initial_board)

    assert game_board.check_if_pawn_in_mill((1, 1)) == [(1, 1), (2, 1), (3, 1)]
    assert game_board.check_if_pawn_in_mill((2, 1)) == [(1, 1), (2, 1), (3, 1)]
    assert game_board.check_if_pawn_in_mill((3, 1)) == [(1, 1), (2, 1), (3, 1)]

    assert game_board.check_if_pawn_in_mill((1, 3)) == [(1, 3), (2, 3), (3, 3)]
    assert game_board.check_if_pawn_in_mill((2, 3)) == [(1, 3), (2, 3), (3, 3)]
    assert game_board.check_if_pawn_in_mill((3, 3)) == [(1, 3), (2, 3), (3, 3)]

    assert game_board.check_if_pawn_in_mill((3, 5)) is None
