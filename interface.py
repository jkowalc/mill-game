from pawn_position_mapper import get_alphabet_from_position_tuple, get_position_tuple_from_alphabet

from player import Player


def get_game_variant() -> int:
    print("\nPossible variants:\n1. Three men's morris\n2. Six men's morris\n3. Nine men's morris\n4. Twelve men's morris")
    inp = input("Choose one: ")
    if inp not in {"1", "2", "3", "4"}:
        print("Wrong value")
        return get_game_variant()
    else:
        return {"1": 3, "2": 6, "3": 9, "4": 12}[inp]


def get_game_mode() -> str:
    print("\nPossible game modes:\n1. Player vs Player\n2. Player vs Computer\n3. Player vs Smart Computer")
    inp = input("Choose one: ")
    if inp not in {"1", "2", "3"}:
        print("Wrong value")
        return get_game_mode()
    else:
        return int(inp)


def get_player_name(letter="", previous_name=None) -> str:
    inp = input(f"\nEnter player{letter}'s name: ")
    if inp == previous_name:
        print("Names cannot be the same")
        return get_player_name(letter, previous_name)
    return inp


def get_player_move(moves: dict, player: Player, board):
    possible_sources = moves.keys()
    source = get_source(possible_sources, player, board)
    possible_destinations = moves[source]
    dest = get_destination(possible_destinations, player, board)
    return (source, dest)


def get_source(positions, player, board):
    for i, pawn in enumerate(positions):
        positions[i] = get_alphabet_from_position_tuple(pawn)
    positions_list = "Possible pawns: ["
    for pos in positions:
        positions_list += f"{pos}, "
    positions_list = positions_list[:-1]
    positions_list += "]"
    print(positions_list)
    inp = input(f"{player.name} choose pawn to move: ")
    if inp not in positions:
        return get_source(positions, player)
    else:
        return get_position_tuple_from_alphabet(inp, board)


def get_destination(positions, player, board):
    for i, pawn in enumerate(positions):
        positions[i] = get_alphabet_from_position_tuple(pawn)
    positions_list = "Possible destinations: ["
    for pos in positions:
        positions_list += f"{pos}, "
    positions_list = positions_list[:-1]
    positions_list += "]"
    print(positions_list)
    inp = input(f"{player.name} choose destination: ")
    if inp not in positions:
        return get_source(positions, player)
    else:
        return get_position_tuple_from_alphabet(inp, board)


def print_winner(player):
    print(f"Player {player.name} won! ")


def print_tie():
    print("The game is tied!")
