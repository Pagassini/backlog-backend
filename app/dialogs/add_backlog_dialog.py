from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QComboBox, QPushButton, QMessageBox
from api.games import fetch_games
from dialogs.add_game_dialog import AddGameDialog

class AddBacklogDialog(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.selected_game_id = None
        self.setLayout(QVBoxLayout())
        self._setup_ui()
        self._load_games()
        self.add_game_button = QPushButton('Add Game')
        self.add_game_button.clicked.connect(self.add_game_dialog)
        self.layout().addWidget(self.add_game_button)
        
    def _setup_ui(self):
        self.setWindowTitle("Add Backlog")
        self.setLayout(QVBoxLayout())

        form_layout = QFormLayout()
        self.game_combo = QComboBox()
        form_layout.addRow("Game:", self.game_combo)
        self.layout().addLayout(form_layout)

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self._add_backlog)
        self.layout().addWidget(self.add_button)

    def _load_games(self):
        games = fetch_games()
        self.games = {game['title']: game['_id'] for game in games}
        self.game_combo.addItems(self.games.keys())

    def _add_backlog(self):
        selected_game_title = self.game_combo.currentText()
        self.selected_game_id = self.games[selected_game_title]
        self.accept()
        
    def add_game_dialog(self):
        dialog = AddGameDialog(self)
        dialog.exec_()
        
    def get_data(self):
        return {
            'game_id': self.selected_game_id,
            'user_id': self.user_id,
            'status': 'playing'
        }
