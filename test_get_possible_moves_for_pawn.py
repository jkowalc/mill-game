from player import Player
from game_boards.three_pawn_board import ThreePawnBoard


def test_get_possible_moves_for_pawn_three():
    playerA = Player("Jan Kowalski", "A", pawns_on_board=[(1, 2), (1, 4), (1, 7)])
    playerB = Player("Agnieszka Nowak", "B", pawns_on_board=[(1, 0), (1, 1), (1, 6)])
    initial_board = [[None],
                     [playerB, playerB, playerA, None, playerA, None, playerB, playerA]]
    game_board = ThreePawnBoard(initial_board)
    playerA.board = game_board
    playerB.board = game_board
    assert game_board.get_possible_moves_for_pawn((1, 1)) == [(0, 0)]
    assert playerB.get_possible_moves() == {(1, 0): [(0, 0)], (1, 1): [(0, 0)], (1, 6):[(1, 5), (0, 0)]}