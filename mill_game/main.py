from game import Game
from interface import (get_game_mode, get_game_variant,
                       get_player_name, print_first_player, GameMode)
import random


def main():
    pawns_num = get_game_variant()
    mode = get_game_mode()
    if mode == GameMode.PLAYER_VS_PLAYER:
        player_a_name = get_player_name("A")
        player_b_name = get_player_name("B", player_a_name)
        player_names = [player_a_name, player_b_name]
    else:
        player_names = [get_player_name()]
    game = Game(mode, player_names, pawns_num)
    first_player = random.choice([game.player_a, game.player_b])
    print_first_player(first_player)
    game.execute_turn(first_player)


if __name__ == "__main__":
    main()
