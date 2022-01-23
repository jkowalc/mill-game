from game_boards.three_pawn_board import ThreePawnBoard
from game_boards.six_pawn_board import SixPawnBoard
from game_boards.nine_pawn_board import NinePawnBoard
from game_boards.twelve_pawn_board import TwelvePawnBoard
from player import Player


def test_check_if_pawn_in_mill_sides():
    playerA = Player("Jan Kowalski", "A")
    playerB = Player("Agnieszka Nowak", "B")
    initial_board = [[None],
                     [None, playerB, playerA, playerA, playerA, None, None, None],
                     [None, None, None, None, playerB, playerB, playerB, None],
                     [None, None, None, None, None, None, None, None]]
    game_board = NinePawnBoard(initial_board)

    # playerA
    assert game_board.get_mills_containing_pawn((1, 2)) == [((1, 2), (1, 3), (1, 4))]
    assert game_board.get_mills_containing_pawn((1, 3)) == [((1, 2), (1, 3), (1, 4))]
    assert game_board.get_mills_containing_pawn((1, 4)) == [((1, 2), (1, 3), (1, 4))]

    # player B
    assert game_board.get_mills_containing_pawn((2, 4)) == [((2, 4), (2, 5), (2, 6))]
    assert game_board.get_mills_containing_pawn((2, 5)) == [((2, 4), (2, 5), (2, 6))]
    assert game_board.get_mills_containing_pawn((2, 6)) == [((2, 4), (2, 5), (2, 6))]

    assert game_board.get_mills_containing_pawn((1, 1)) == []


def test_check_if_pawn_in_mill_sides_6_pawns():
    playerA = Player("Jan Kowalski", "A")
    playerB = Player("Agnieszka Nowak", "B")
    initial_board = [[None],
                     [None, playerB, playerA, playerA, playerA, None, None, None],
                     [None, None, None, None, playerB, playerB, playerB, None]]
    game_board = SixPawnBoard(initial_board)

    # playerA
    assert game_board.get_mills_containing_pawn((1, 2)) == [((1, 2), (1, 3), (1, 4))]
    assert game_board.get_mills_containing_pawn((1, 3)) == [((1, 2), (1, 3), (1, 4))]
    assert game_board.get_mills_containing_pawn((1, 4)) == [((1, 2), (1, 3), (1, 4))]

    # player B
    assert game_board.get_mills_containing_pawn((2, 4)) == [((2, 4), (2, 5), (2, 6))]
    assert game_board.get_mills_containing_pawn((2, 5)) == [((2, 4), (2, 5), (2, 6))]
    assert game_board.get_mills_containing_pawn((2, 6)) == [((2, 4), (2, 5), (2, 6))]

    assert game_board.get_mills_containing_pawn((1, 1)) == []


def test_check_if_pawn_in_mill_diagonals_12_pawns():
    playerA = Player("Jan Kowalski", "A")
    playerB = Player("Agnieszka Nowak", "B")
    initial_board = [[None],
                     [None, None, playerA, None, playerB, None, None, None],
                     [None, None, playerA, None, playerB, None, None, None],
                     [None, None, playerA, None, playerB, None, None, None]]
    game_board = TwelvePawnBoard(initial_board)

    assert game_board.get_mills_containing_pawn((1, 2)) == [((1, 2), (2, 2), (3, 2))]
    assert game_board.get_mills_containing_pawn((2, 2)) == [((1, 2), (2, 2), (3, 2))]
    assert game_board.get_mills_containing_pawn((3, 2)) == [((1, 2), (2, 2), (3, 2))]

    assert game_board.get_mills_containing_pawn((1, 4)) == [((1, 4), (2, 4), (3, 4))]
    assert game_board.get_mills_containing_pawn((2, 4)) == [((1, 4), (2, 4), (3, 4))]
    assert game_board.get_mills_containing_pawn((3, 4)) == [((1, 4), (2, 4), (3, 4))]

    assert game_board.get_mills_containing_pawn((1, 7)) == []


def test_check_if_pawn_in_mill_diagonals_9_pawns():
    playerA = Player("Jan Kowalski", "A")
    playerB = Player("Agnieszka Nowak", "B")
    initial_board = [[None],
                     [None, None, playerA, None, playerB, None, None, None],
                     [None, None, playerA, None, playerB, None, None, None],
                     [None, None, playerA, None, playerB, None, None, None]]
    game_board = NinePawnBoard(initial_board)

    assert game_board.get_mills_containing_pawn((1, 2)) == []
    assert game_board.get_mills_containing_pawn((2, 2)) == []
    assert game_board.get_mills_containing_pawn((3, 2)) == []

    assert game_board.get_mills_containing_pawn((1, 4)) == []
    assert game_board.get_mills_containing_pawn((2, 4)) == []
    assert game_board.get_mills_containing_pawn((3, 4)) == []

    assert game_board.get_mills_containing_pawn((1, 7)) == []


def test_check_if_pawn_in_mill_diff_rectangle_12_pawns():
    playerA = Player("Jan Kowalski", "A")
    playerB = Player("Agnieszka Nowak", "B")
    initial_board = [[None],
                     [None, playerA, None, playerB, None, None, None, None],
                     [None, playerA, None, playerB, None, None, None, None],
                     [None, playerA, None, playerB, None, playerB, None, None]]
    game_board = TwelvePawnBoard(initial_board)

    assert game_board.get_mills_containing_pawn((1, 1)) == [((1, 1), (2, 1), (3, 1))]
    assert game_board.get_mills_containing_pawn((2, 1)) == [((1, 1), (2, 1), (3, 1))]
    assert game_board.get_mills_containing_pawn((3, 1)) == [((1, 1), (2, 1), (3, 1))]

    assert game_board.get_mills_containing_pawn((1, 3)) == [((1, 3), (2, 3), (3, 3))]
    assert game_board.get_mills_containing_pawn((2, 3)) == [((1, 3), (2, 3), (3, 3))]
    assert game_board.get_mills_containing_pawn((3, 3)) == [((1, 3), (2, 3), (3, 3))]

    assert game_board.get_mills_containing_pawn((3, 5)) == []


def test_check_if_pawn_in_mill_diff_rectangle_9_pawns():
    playerA = Player("Jan Kowalski", "A")
    playerB = Player("Agnieszka Nowak", "B")
    initial_board = [[None],
                     [None, playerA, None, playerB, None, None, None, None],
                     [None, playerA, None, playerB, None, None, None, None],
                     [None, playerA, None, playerB, None, playerB, None, None]]
    game_board = NinePawnBoard(initial_board)

    assert game_board.get_mills_containing_pawn((1, 1)) == [((1, 1), (2, 1), (3, 1))]
    assert game_board.get_mills_containing_pawn((2, 1)) == [((1, 1), (2, 1), (3, 1))]
    assert game_board.get_mills_containing_pawn((3, 1)) == [((1, 1), (2, 1), (3, 1))]

    assert game_board.get_mills_containing_pawn((1, 3)) == [((1, 3), (2, 3), (3, 3))]
    assert game_board.get_mills_containing_pawn((2, 3)) == [((1, 3), (2, 3), (3, 3))]
    assert game_board.get_mills_containing_pawn((3, 3)) == [((1, 3), (2, 3), (3, 3))]

    assert game_board.get_mills_containing_pawn((3, 5)) == []
