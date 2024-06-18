
class PlatformException(Exception):
    def __init__(self, message: str = "An Error has occurred", name: str = "Platform"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)


class PlatformNotFoundException(PlatformException):
    def __init__(self):
        self.message = f"One or more platforms not found."
        super().__init__(self.message)