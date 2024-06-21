class BacklogException(Exception):
    def __init__(self, message: str = "An Error has occurred", name: str = "Backlog"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)

class BacklogNotFoundException(BacklogException):
    def __init__(self):
        self.message = f"Backlog not found."
        super().__init__(self.message)

class UserHasGameException(BacklogException):
    def __init__(self):
        self.message = f"This user already have the game on the backlog."
        super().__init__(self.message)