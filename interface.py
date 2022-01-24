from copy import deepcopy
from pawn_position_mapper import (get_alphabet_from_position_tuple,
                                  get_position_tuple_from_alphabet)


def get_game_variant() -> int:
    print("""\nPossible variants:
    1. Three men's morris
    2. Six men's morris
    3. Nine men's morris
    4. Twelve men's morris""")
    inp = input("Choose one: ")
    if inp not in {"1", "2", "3", "4"}:
        print("Wrong value")
        return get_game_variant()
    else:
        return {"1": 3, "2": 6, "3": 9, "4": 12}[inp]


def get_game_mode() -> str:
    print("""\nPossible game modes:
    1. Player vs Player
    2. Player vs Computer
    3. Player vs Smart Computer""")
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


def get_player_move(moves: dict, player, board):
    possible_sources = list(moves.keys())
    source = get_source(possible_sources, player, board)
    possible_destinations = moves[source]
    dest = get_destination(possible_destinations, player, board)
    return (source, dest)


def get_source(positions, player, board):
    positions_alphabet = deepcopy(positions)
    for i, pawn in enumerate(positions):
        positions_alphabet[i] = get_alphabet_from_position_tuple(pawn, board)
    return get_source_loop(positions_alphabet, player, board)


def get_source_loop(positions, player, board):
    print(positions)
    inp = input(f"{player.name} choose pawn to move: ")
    if inp not in positions:
        print("Wrong value")
        return get_source_loop(positions, player, board)
    else:
        return get_position_tuple_from_alphabet(inp, board)


def get_destination(positions, player, board):
    positions_alphabet = deepcopy(positions)
    for i, pawn in enumerate(positions):
        positions_alphabet[i] = get_alphabet_from_position_tuple(pawn, board)
    return get_destination_loop(positions_alphabet, player, board)


def get_destination_loop(positions, player, board):
    print(positions)
    inp = input(f"{player.name} choose destination: ")
    if inp not in positions:
        print("Wrong value")
        return get_destination_loop(positions, player, board)
    else:
        return get_position_tuple_from_alphabet(inp, board)


def get_pawn_to_take(positions, player, board):
    positions_alphabet = deepcopy(positions)
    for i, pawn in enumerate(positions):
        positions_alphabet[i] = get_alphabet_from_position_tuple(pawn, board)
    return get_pawn_to_take_loop(positions_alphabet, player, board)


def get_pawn_to_take_loop(positions, player, board):
    print(positions)
    inp = input(f"Choose one of {player.name}'s pawns to take out: ")
    if inp not in positions:
        print("Wrong value")
        return get_pawn_to_take_loop(positions, player, board)
    else:
        return get_position_tuple_from_alphabet(inp, board)


def print_move(player, move, board):
    source, dest = move
    source_alphabet = get_alphabet_from_position_tuple(source, board)
    dest_alphabet = get_alphabet_from_position_tuple(dest, board)
    print(f"\n{player.name} moved from {source_alphabet} to {dest_alphabet}")


def print_take_out(player, pawn_position, board):
    pawn_alphabet = get_alphabet_from_position_tuple(pawn_position, board)
    print(f"{player.name}'s {pawn_alphabet} pawn has been taken out")


def print_take_in(player, pawn_position, board):
    pawn_alphabet = get_alphabet_from_position_tuple(pawn_position, board)
    print(f"{player.name} placed his pawn on {pawn_alphabet}")


def print_winner(player):
    print(f"\nPlayer {player.name} won! ")


def print_tie():
    print("\nThe game is tied!")


def print_first_player(player):
    print(f"\n{player.name} is starting")
