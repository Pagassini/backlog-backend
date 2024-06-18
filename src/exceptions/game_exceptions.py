class GameException(Exception):
    def __init__(self, message: str = "An Error has occurred", name: str = "Game"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)

class GameNotFoundException(GameException):
    def __init__(self):
        self.message = f"One or more games not found."
        super().__init__(self.message)