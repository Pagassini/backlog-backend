
class GenreException(Exception):
    def __init__(self, message: str = "An Error has occurred", name: str = "Genre"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)


class GenreNotFoundException(GenreException):
    def __init__(self):
        self.message = f"One or more Genres not found."
        super().__init__(self.message)
        
class GenreAlreadyExistsException(GenreException):
    def __init__(self):
        self.message = f"Genre already exists."
        super().__init__(self.message)