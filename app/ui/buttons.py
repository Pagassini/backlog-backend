from PyQt5.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

class AddBacklogButton(Button):
    def __init__(self, parent=None):
        super().__init__("Add Backlog", parent)

class UpdateBacklogButton(Button):
    def __init__(self, parent=None):
        super().__init__("Update Backlog", parent)

class DeleteBacklogButton(Button):
    def __init__(self, parent=None):
        super().__init__("Delete Backlog", parent)