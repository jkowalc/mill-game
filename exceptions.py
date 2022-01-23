class InvalidPawnPositionError(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)


class InvalidInitialBoardError(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)


class WrongPawnNumberError(Exception):
    def __init__(self):
        msg = "Pawn number must be either 3, 6, 9 or 12"
        super().__init__(msg)