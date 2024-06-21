class UserException(Exception):
    def __init__(self, message: str = "An Error has occurred", name: str = "User"):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)


class UserNameAlreadyExistsException(UserException):
    def __init__(self):
        self.message = f"A user with the same name already exists"
        super().__init__(self.message)

class EmailAlreadyExistsException(UserException):
    def __init__(self):
        self.message = f"this email already exists"
        super().__init__(self.message)

class UserNotFoundException(UserException):
    def __init__(self):
        self.message = f"User not found."
        super().__init__(self.message)