class BacklogException(Exception):
    def __init__(self, message: str = "An Error has occurred", name: str = "Backlog"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)

class BacklogNotFoundException(BacklogException):
    def __init__(self):
        self.message = f"Backlog not found."
        super().__init__(self.message)