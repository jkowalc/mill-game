from game import Game
from interface import get_game_mode, get_game_variant, get_player_name
from player import ComputerPlayer, Player, SmartComputerPlayer


def main():
    pawns_num = get_game_variant()
    mode = get_game_mode()
    if mode == 1:
        playerA = Player(get_player_name(" A"), "A", pawns_num)
        playerB = Player(get_player_name(" B"), "B", pawns_num)
    elif mode == 2:
        playerA = Player(get_player_name(), "P", pawns_num)
        playerB = ComputerPlayer("C", pawns_num)
    elif mode == 3:
        playerA = Player(get_player_name(), "P", pawns_num)
        playerB = SmartComputerPlayer("C", pawns_num)
    game = Game(playerA, playerB, pawns_num)


if __name__ == "__main__":
    main()
