from __future__ import annotations

from enum import Enum

from mill_game.exceptions import WrongPawnNumberError
from mill_game import interface
import random

from mill_game.game_board import GameBoard


class PlayerColor(Enum):
    WHITE = 1
    BLACK = 2

    def __str__(self):
        if self == PlayerColor.WHITE:
            return '\u25CB'
        elif self == PlayerColor.BLACK:
            return '\u25CF'
        else:
            raise ValueError()


class Player:
    def __init__(self, board: GameBoard, name: str, symbol: PlayerColor, pawns_num: int = 9, pawns_on_board: list[tuple[int, int]] = None):
        self.board = board
        self.name = name
        self.symbol = symbol
        if pawns_num not in {3, 6, 9, 12}:
            raise WrongPawnNumberError
        self.pawns_num = pawns_num
        self.pawns_on_board: list[tuple[int, int]] = pawns_on_board if pawns_on_board else []

    def can_jump(self) -> bool:
        return self.pawns_num == 3

    def has_placed_all_pawns(self) -> bool:
        return len(self.pawns_on_board) == self.pawns_num

    def get_possible_pawns_to_take(self):
        possible_pawns = []
        for pawn in self.pawns_on_board:
            if not self.board.check_if_pawn_in_mill(pawn):
                possible_pawns.append(pawn)
        return possible_pawns

    def get_possible_moves(self):
        moves = {}
        for pawn in self.pawns_on_board:
            if self.can_jump():
                moves_for_pawn = self.board.get_all_empty_pawn_positions()
            else:
                moves_for_pawn = self.board.get_possible_moves_for_pawn(pawn)
            if len(moves_for_pawn) > 0:
                moves[pawn] = moves_for_pawn
        return moves

    def execute_move(self, move: tuple[tuple[int, int] | None, tuple[int, int] | None]):
        source, dest = move
        if source:
            self.pawns_on_board.remove(source)
        if dest:
            self.pawns_on_board.append(dest)

    def select_move(self, moves: dict):
        return interface.get_player_move(moves, self, self.board)

    def select_destination(self, possible_destinations):
        return interface.get_destination(possible_destinations, self,
                                         self.board)

    def select_pawn_to_take(self, possible_pawns, other_player):
        return interface.get_pawn_to_take(possible_pawns, other_player,
                                          self.board)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Player):
            return self.name == __o.name
        else:
            return False

    def __str__(self):
        return self.symbol


class ComputerPlayer(Player):
    def __init__(self, board: GameBoard, symbol: PlayerColor, pawns_num=9, pawns_on_board=None, name=None):
        if not name:
            name = "Computer"
        super().__init__(board, name, symbol, pawns_num, pawns_on_board)

    def select_move(self, moves: dict):
        source = random.choice(list(moves.keys()))
        possible_destinations = moves[source]
        dest = random.choice(possible_destinations)
        return source, dest

    def select_destination(self, possible_destinations):
        return random.choice(possible_destinations)

    def select_pawn_to_take(self, possible_pawns, other_player):
        return random.choice(possible_pawns)


class SmartComputerPlayer(ComputerPlayer):
    def __init__(self, board: GameBoard, symbol: PlayerColor, pawns_num: int = 9, pawns_on_board: list[tuple[int, int]] = None):
        name = "Smart Computer"
        super().__init__(board, symbol, pawns_num, pawns_on_board, name)

    def select_move(self, moves: dict):
        return super().select_move(moves)

    def select_destination(self, possible_destinations):
        return super().select_destination(possible_destinations)

    def select_pawn_to_take(self, possible_pawns, other_player):
        return super().select_pawn_to_take(possible_pawns, other_player)
