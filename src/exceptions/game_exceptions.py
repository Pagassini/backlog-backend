class GameException(Exception):
    def __init__(self, message: str = "An Error has occurred", name: str = "Game"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)

class GameNotFoundException(GameException):
    def __init__(self):
        self.message = f"Game not found."
        super().__init__(self.message)
        
class GameAlreadyExistsException(GameException):
    def __init__(self):
        self.message = f"A game with the same title already exists"
        super().__init__(self.message)