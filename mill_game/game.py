from exceptions import WrongPawnNumberError
from game_boards.nine_pawn_board import NinePawnBoard
from game_boards.six_pawn_board import SixPawnBoard
from game_boards.three_pawn_board import ThreePawnBoard
from game_boards.twelve_pawn_board import TwelvePawnBoard
from player import Player
import interface
from copy import deepcopy


class Game:
    def __init__(self, player_a: Player, player_b: Player, pawns_num: int):
        if pawns_num == 12:
            self.board = TwelvePawnBoard()
        elif pawns_num == 9:
            self.board = NinePawnBoard()
        elif pawns_num == 6:
            self.board = SixPawnBoard()
        elif pawns_num == 3:
            self.board = ThreePawnBoard()
        self.player_a = player_a
        self.player_b = player_b
        self.player_a.board = self.board
        self.player_b.board = self.board

        if pawns_num not in {3, 6, 9, 12}:
            raise WrongPawnNumberError
        self.pawns_num = pawns_num
        self.number_of_rounds_from_last_mill = 0
        self.previous_boards = [deepcopy(self.board)]

    def check_pawn_num_condition(self) -> bool:
        if self.player_a.pawns_num <= 2:
            self.announce_victory(self.player_b)
            return True
        if self.player_b.pawns_num <= 2:
            self.announce_victory(self.player_a)
            return True
        return False

    def check_winning_conditions(self) -> bool:
        return self.check_pawn_num_condition()

    def save_board_config(self):
        self.previous_boards.append(deepcopy(self.board))

    def check_board_config_condition(self) -> bool:
        number_of_eq = 0
        for previous_board in self.previous_boards:
            if previous_board == self.board:
                number_of_eq += 1
        return number_of_eq >= 3

    def check_tie_conditions(self) -> bool:
        return all([
            self.number_of_rounds_from_last_mill >= 40,
            self.check_board_config_condition()
        ])

    @staticmethod
    def announce_victory(player):
        interface.print_winner(player)

    @staticmethod
    def announce_tie():
        interface.print_tie()

    def get_other_player(self, player: Player):
        if player == self.player_a:
            return self.player_b
        elif player == self.player_b:
            return self.player_a

    def take_out_pawn(self, player: Player):
        other_player = self.get_other_player(player)
        pawns_to_take = other_player.get_possible_pawns_to_take()
        selected = player.select_pawn_to_take(pawns_to_take, other_player)
        self.board.take_out_pawn(selected)
        other_player.execute_move((selected, None))
        interface.print_take_out(other_player, selected, self.board)
        other_player.pawns_num -= 1
        self.number_of_rounds_from_last_mill = 0

    def execute_turn_first_phase(self, player: Player):
        possible_destinations = self.board.get_all_empty_pawn_positions()
        selected = player.select_destination(possible_destinations)
        self.board.place_pawn(selected, player)
        player.execute_move((None, selected))
        interface.print_take_in(player, selected, self.board)
        dest = selected
        if self.board.check_if_pawn_in_mill(dest):
            self.take_out_pawn(player)

    def execute_turn_second_phase(self, player: Player):
        moves = player.get_possible_moves()
        if len(moves) == 0:
            self.announce_victory(self.get_other_player(player))
        selected = player.select_move(moves)
        self.board.execute_move(selected)
        player.execute_move(selected)
        interface.print_move(player, selected, self.board)
        dest = selected[1]
        if self.board.check_if_pawn_in_mill(dest):
            self.take_out_pawn(player)

    def execute_turn(self, player: Player):
        print(self.board)
        self.number_of_rounds_from_last_mill += 1
        if player.has_placed_all_pawns():
            self.execute_turn_second_phase(player)
        else:
            self.execute_turn_first_phase(player)
        self.save_board_config()
        if not (self.check_winning_conditions() or
                self.check_tie_conditions()):
            self.execute_turn(self.get_other_player(player))
