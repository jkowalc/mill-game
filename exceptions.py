class InvalidPawnPositionError(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)


class InvalidInitialBoardError(Exception):
    def __init__(self, msg=None):
        super().__init__(msg)
