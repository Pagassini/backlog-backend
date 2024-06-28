from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QDialogButtonBox
from PyQt5.QtCore import Qt

class AddBacklogDialog(QDialog):
    BACKGROUND_COLOR = "#2e2e2e"
    TEXT_COLOR = "white"
    STATUS_OPTIONS = ['finished', 'playing', 'dropped', 'completed']

    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id

        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle('Add Backlog')
        self.setStyleSheet(f"background-color: {self.BACKGROUND_COLOR}; color: {self.TEXT_COLOR};")

        self.layout = QVBoxLayout(self)
        
        self._add_game_id_input()
        self._add_status_input()
        self._add_button_box()

    def _add_game_id_input(self):
        game_id_label = QLabel('Game ID:')
        self.game_id_input = QLineEdit('', self)
        self.layout.addWidget(game_id_label)
        self.layout.addWidget(self.game_id_input)

    def _add_status_input(self):
        status_label = QLabel('Status:')
        self.status_input = QComboBox(self)
        self.status_input.addItems(self.STATUS_OPTIONS)
        self.layout.addWidget(status_label)
        self.layout.addWidget(self.status_input)

    def _add_button_box(self):
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

    def get_data(self):
        return {
            'game_id': self.game_id_input.text(),
            'user_id': self.user_id,
            'status': self.status_input.currentText()
        }
