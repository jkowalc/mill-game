from turtle import pos
from exceptions import WrongPawnNumberError
from game_boards.game_board import GameBoard
from game_boards.nine_pawn_board import NinePawnBoard
from game_boards.six_pawn_board import SixPawnBoard
from game_boards.three_pawn_board import ThreePawnBoard
from game_boards.twelve_pawn_board import TwelvePawnBoard
from player import ComputerPlayer, Player
import interface

class Game:
    def __init__(self, playerA: Player, playerB: Player, pawns_num):
        self.playerA = playerA
        self.playerB = playerB
        if pawns_num not in {3, 6, 9, 12}:
            raise WrongPawnNumberError
        self.pawns_num = pawns_num
        self.game_phase = 1
        self.init_board()

    def init_board(self):
        if self.pawns_num == 12:
            self.board = TwelvePawnBoard()
        elif self.pawns_num == 9:
            self.board = NinePawnBoard()
        elif self.pawns_num == 6:
            self.board = SixPawnBoard()
        elif self.pawns_num == 3:
            self.board = ThreePawnBoard()
        self.playerA.board = self.board
        self.playerB.board = self.board

    def check_pawn_num_condition(self):
        if self.playerA.pawns_num <= 2:
            self.announce_victory(self.playerA)
            return True
        if self.playerB.pawns_num <= 2:
            self.announce_victory(self.playerB)
            return True
        return False

    def check_winning_conditions(self):
        conditions = [
            self.check_pawn_num_condition()
        ]
        return False not in conditions

    def announce_victory(self, player):
        interface.print_winner(player)

    def announce_tie(self):
        interface.print_tie()

    def check_tie_conditions(self):
        pass

    def get_other_player(self, player):
        if player == self.playerA:
            return self.playerB
        elif player == self.playerB:
            return self.playerA

    def execute_turn_first_phase(self, player):
        possible_destinations = self.board.get_all_empty_pawn_positions()
        selected = player.select_destination(possible_destinations)
        self.board.place_pawn(selected, player)
        player.execute_move((None, selected))
        dest = selected
        if self.board.check_if_pawn_in_mill(dest):
            pass  # remove one opponent's pawn

    def execute_turn_second_phase(self, player):
        moves = self.board.get_possible_moves_for_player(player)
        selected = player.select_move(moves)
        self.board.execute_move(selected)
        player.execute_move(selected)
        dest = selected[1]
        if self.board.check_if_pawn_in_mill(dest):
            pass  # remove one opponent's pawn

    def execute_turn(self, player: Player):
        if player.has_placed_all_pawns():
            self.execute_turn_second_phase(player)
        else:
            self.execute_turn_first_phase(player)
        if not (self.check_winning_conditions() or self.check_tie_conditions()):
            self.execute_turn(self.get_other_player(player))