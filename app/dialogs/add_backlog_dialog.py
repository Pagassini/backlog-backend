import os
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QComboBox, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon
from api.games import fetch_games
from dialogs.add_game_dialog import AddGameDialog

class AddBacklogDialog(QDialog):
    ICONS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icons")
    
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.user_id = user_id
        self.selected_game_id = None
        self.setLayout(QVBoxLayout())
        self._setup_ui()
        self._load_games()
        
    def _setup_ui(self):
        self.setWindowTitle("Add Backlog")

        form_layout = QFormLayout()
        self.game_combo = QComboBox()
        form_layout.addRow(self.game_combo)
        
        self.add_game_button = QPushButton(QIcon(os.path.join(self.ICONS_PATH, 'Add.png')), '')
        self.add_game_button.clicked.connect(self.add_game_dialog)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.game_combo)
        button_layout.addWidget(self.add_game_button)
        
        self.layout().addLayout(button_layout)
        self.layout().addLayout(form_layout)

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self._add_backlog)
        self.layout().addWidget(self.add_button)

    def _load_games(self):
        self.game_combo.clear()
        games = fetch_games()
        self.games = {game['title']: game['_id'] for game in games}
        self.game_combo.addItems(self.games.keys())

    def _add_backlog(self):
        selected_game_title = self.game_combo.currentText()
        self.selected_game_id = self.games[selected_game_title]
        self.accept()
        
    def add_game_dialog(self):
        dialog = AddGameDialog(self)
        dialog.game_added.connect(self._load_games)
        dialog.exec_()
        
    def get_data(self):
        return {
            'game_id': self.selected_game_id,
            'user_id': self.user_id,
            'status': 'playing'
        }
