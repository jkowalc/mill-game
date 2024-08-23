from game import Game
from interface import (get_game_mode, get_game_variant,
                       get_player_name, print_first_player, GameMode)
from player import ComputerPlayer, Player, SmartComputerPlayer
import random


def main():
    pawns_num = get_game_variant()
    mode = get_game_mode()
    player_a = None
    player_b = None
    if mode == GameMode.PLAYER_VS_PLAYER:
        player_a = Player(get_player_name("A"), "A", pawns_num)
        previous_name = player_a.name
        player_b = Player(get_player_name("B", previous_name), "B", pawns_num)
    elif mode == GameMode.PLAYER_VS_COMPUTER:
        player_a = Player(get_player_name(), "P", pawns_num)
        player_b = ComputerPlayer("C", pawns_num)
    elif mode == GameMode.PLAYER_VS_SMART_COMPUTER:
        player_a = Player(get_player_name(), "P", pawns_num)
        player_b = SmartComputerPlayer("C", pawns_num)
    game = Game(player_a, player_b, pawns_num)
    first_player = random.choice([player_a, player_b])
    print_first_player(first_player)
    game.execute_turn(first_player)


if __name__ == "__main__":
    main()
