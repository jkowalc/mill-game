from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mill_game.game_board import GameBoard
    from mill_game.player import Player, PlayerColor
from mill_game.pawn_position_mapper import (
    get_alphabet_from_position_tuple,
    get_position_tuple_from_alphabet,
)


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


class GameMode(Enum):
    PLAYER_VS_PLAYER = 1
    PLAYER_VS_COMPUTER = 2
    PLAYER_VS_SMART_COMPUTER = 3


def get_game_mode() -> GameMode:
    inp = ""
    while inp not in {"1", "2", "3"}:
        print("""\nPossible game modes:
            1. Player vs Player
            2. Player vs Computer
            3. Player vs Smart Computer""")
        inp = input("Choose one: ")
    return GameMode(int(inp))


def get_player_name(color: PlayerColor, previous_name: str | None = None) -> str:
    inp = input(f"\nEnter {color.name.lower()} player's name: ")
    if previous_name and inp == previous_name:
        print("Names cannot be the same")
        return get_player_name(color, previous_name)
    return inp


def get_player_move(
    moves: dict, player: Player, board: GameBoard
) -> tuple[tuple[int, int], tuple[int, int]]:
    possible_sources = list(moves.keys())
    source = get_source(possible_sources, player, board)
    possible_destinations = moves[source]
    dest = get_destination(possible_destinations, player, board)
    return source, dest


def get_source(
    positions: list[tuple[int, int]], player: Player, board: GameBoard
) -> tuple[int, int]:
    positions_readable = [
        get_alphabet_from_position_tuple(pos, board) for pos in positions
    ]
    print(positions_readable)
    choice = None
    while choice is None:
        inp = input(f"{player.name} choose pawn to move: ")
        if inp in positions_readable:
            choice = get_position_tuple_from_alphabet(inp, board)
        else:
            print("Wrong value")
    return choice


def get_destination(
    positions: list[tuple[int, int]], player: Player, board: GameBoard
) -> tuple[int, int]:
    positions_readable = [
        get_alphabet_from_position_tuple(pos, board) for pos in positions
    ]
    print(positions_readable)
    choice = None
    while choice is None:
        inp = input(f"{player.name} choose destination: ")
        if inp in positions_readable:
            choice = get_position_tuple_from_alphabet(inp, board)
        else:
            print("Wrong value")
    return choice


def get_pawn_to_take(
    positions: list[tuple[int, int]], player: Player, board: GameBoard
) -> tuple[int, int]:
    positions_readable = [
        get_alphabet_from_position_tuple(pos, board) for pos in positions
    ]
    print(positions_readable)
    inp = None
    choice = None
    while choice is None:
        inp = input(f"Choose one of {player.name}'s pawns to take out: ")
        if inp in positions_readable:
            choice = get_position_tuple_from_alphabet(inp, board)
        else:
            print("Wrong value")
    return choice


def print_move(
    player: Player, move: tuple[tuple[int, int], tuple[int, int]], board: GameBoard
):
    source, dest = move
    source_alphabet = get_alphabet_from_position_tuple(source, board)
    dest_alphabet = get_alphabet_from_position_tuple(dest, board)
    print(f"\n{player.name} moved from {source_alphabet} to {dest_alphabet}")


def print_take_out(player: Player, pawn_position: tuple[int, int], board: GameBoard):
    pawn_alphabet = get_alphabet_from_position_tuple(pawn_position, board)
    print(f"{player.name}'s {pawn_alphabet} pawn has been taken out")


def print_take_in(player: Player, pawn_position: tuple[int, int], board: GameBoard):
    pawn_alphabet = get_alphabet_from_position_tuple(pawn_position, board)
    print(f"{player.name} placed his pawn on {pawn_alphabet}")


def print_winner(player: Player):
    print(f"\nPlayer {player.name} won! ")


def print_tie():
    print("\nThe game is tied!")


def print_first_player(player: Player):
    print(f"\n{player.name} is starting")
