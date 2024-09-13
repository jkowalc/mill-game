from mill_game.player import Player, PlayerColor
from mill_game.game_boards.three_pawn_board import ThreePawnBoard


def test_get_possible_moves_for_pawn_three():
    initial_board = [[None],
                     [PlayerColor.BLACK, PlayerColor.BLACK, PlayerColor.WHITE, None,
                      PlayerColor.WHITE, None, PlayerColor.BLACK, PlayerColor.WHITE]]
    game_board = ThreePawnBoard(initial_board)
    player_black = Player(game_board, "Agnieszka Nowak", PlayerColor.BLACK,
                          pawns_on_board=[(1, 0), (1, 1), (1, 6)])
    assert game_board.get_possible_moves_for_pawn((1, 1)) == [(0, 0)]
    assert player_black.get_possible_moves() == {(1, 0): [(0, 0)],
                                                 (1, 1): [(0, 0)],
                                                 (1, 6): [(1, 5), (0, 0)]}
