from mill_game.player import Player, PlayerSymbol
from mill_game.game_boards.three_pawn_board import ThreePawnBoard


def test_get_possible_moves_for_pawn_three():

    initial_board = [[None],
                     [PlayerSymbol.B, PlayerSymbol.B, PlayerSymbol.A, None,
                      PlayerSymbol.A, None, PlayerSymbol.B, PlayerSymbol.A]]
    game_board = ThreePawnBoard(initial_board)
    player_b = Player(game_board, "Agnieszka Nowak", PlayerSymbol.B,
                      pawns_on_board=[(1, 0), (1, 1), (1, 6)])
    assert game_board.get_possible_moves_for_pawn((1, 1)) == [(0, 0)]
    assert player_b.get_possible_moves() == {(1, 0): [(0, 0)],
                                             (1, 1): [(0, 0)],
                                             (1, 6): [(1, 5), (0, 0)]}
