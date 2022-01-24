from __future__ import annotations
from exceptions import WrongPawnNumberError
from game_boards.game_board import GameBoard
import interface


class Player:
    def __init__(self, name, symbol, pawns_num=9, pawns_on_board=None):
        self.name = name
        self.symbol = symbol
        if pawns_num not in {3, 6, 9, 12}:
            raise WrongPawnNumberError
        self.pawns_num = pawns_num
        self.pawns_on_board = pawns_on_board

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
            moves_for_pawn = []
            if self.can_jump():
                moves_for_pawn = self.board.get_all_empty_pawn_positions()
            else:
                moves_for_pawn = self.board.get_possible_moves_for_pawn(pawn)
            if len(moves_for_pawn) > 0:
                moves[pawn] = moves_for_pawn
        return moves

    def execute_move(self, move):
        source, dest = move
        self.pawns_on_board.remove(source)
        self.pawns_on_board.append(dest)

    def select_move(self, moves: dict):
        return interface.get_player_move(moves, self, self.board)

    def select_destination(self, possible_destinations):
        return interface.get_destination(possible_destinations, self, self.board)

    def select_pawn_to_take(self, possible_pawns):
        return interface.get_pawn_to_take(possible_pawns, self, self.board)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Player):
            return self.name == __o.name
        else:
            return False

    def __str__(self):
        return self.symbol


class ComputerPlayer(Player):
    def __init__(self, symbol, pawns_num=9, pawns_on_board=None):
        name = "Computer"
        super().__init__(name, symbol, pawns_num, pawns_on_board)

    def select_move(self, moves: dict):
        pass

    def select_destination(self, possible_destinations):
        return super().select_destination(possible_destinations)

    def select_pawn_to_take(self, possible_pawns):
        return super().select_pawn_to_take(possible_pawns)


class SmartComputerPlayer(ComputerPlayer):
    def select_move(self, moves: dict):
        pass

    def select_destination(self, possible_destinations):
        return super().select_destination(possible_destinations)

    def select_pawn_to_take(self, possible_pawns):
        return super().select_pawn_to_take(possible_pawns)
