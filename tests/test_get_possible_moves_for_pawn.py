from mill_game.player import Player
from mill_game.game_boards.three_pawn_board import ThreePawnBoard


def test_get_possible_moves_for_pawn_three():
    player_a = Player("Jan Kowalski", "A",
                      pawns_on_board=[(1, 2), (1, 4), (1, 7)])
    player_b = Player("Agnieszka Nowak", "B",
                      pawns_on_board=[(1, 0), (1, 1), (1, 6)])
    initial_board = [[None],
                     [player_b, player_b, player_a, None,
                      player_a, None, player_b, player_a]]
    game_board = ThreePawnBoard(initial_board)
    player_a.board = game_board
    player_b.board = game_board
    assert game_board.get_possible_moves_for_pawn((1, 1)) == [(0, 0)]
    assert player_b.get_possible_moves() == {(1, 0): [(0, 0)],
                                             (1, 1): [(0, 0)],
                                             (1, 6): [(1, 5), (0, 0)]}
