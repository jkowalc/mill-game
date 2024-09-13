from game import Game
from interface import (get_game_mode, get_game_variant,
                       get_player_name, print_first_player, GameMode)
import random

from mill_game.player import PlayerColor


def main():
    pawns_num = get_game_variant()
    mode = get_game_mode()
    if mode == GameMode.PLAYER_VS_PLAYER:
        first_player_name = get_player_name(PlayerColor.WHITE)
        second_player_name = get_player_name(PlayerColor.BLACK, first_player_name)
        player_names = [first_player_name, second_player_name]
    else:
        player_names = [get_player_name(PlayerColor.WHITE)]
    game = Game(mode, player_names, pawns_num)
    first_player = random.choice([game.player_white, game.player_black])
    print_first_player(first_player)
    game.execute_turn(first_player)


if __name__ == "__main__":
    main()
