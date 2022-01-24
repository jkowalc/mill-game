from game import Game
from interface import get_game_mode, get_game_variant, get_player_name, print_first_player
from player import ComputerPlayer, Player, SmartComputerPlayer
import random


def main():
    pawns_num = get_game_variant()
    mode = get_game_mode()
    if mode == 1:
        playerA = Player(get_player_name("A"), "A", pawns_num)
        previous_name = playerA.name
        playerB = Player(get_player_name("B", previous_name), "B", pawns_num)
    elif mode == 2:
        playerA = Player(get_player_name(), "P", pawns_num)
        playerB = ComputerPlayer("C", pawns_num)
    elif mode == 3:
        playerA = Player(get_player_name(), "P", pawns_num)
        playerB = SmartComputerPlayer("C", pawns_num)
    game = Game(playerA, playerB, pawns_num)
    first_player = random.choice([playerA, playerB])
    print_first_player(first_player)
    game.execute_turn(first_player)


if __name__ == "__main__":
    main()
