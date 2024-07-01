from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from api.games import create_games

class AddGameDialog(QDialog):
    game_added = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Game')
        self.setModal(True)
        self.layout = QVBoxLayout(self)

        self.title_label = QLabel('Title:')
        self.title_input = QLineEdit()
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.title_input)

        self.platforms_label = QLabel('Platforms:')
        self.platforms_input = QLineEdit()
        self.layout.addWidget(self.platforms_label)
        self.layout.addWidget(self.platforms_input)

        self.genres_label = QLabel('Genres:')
        self.genres_input = QLineEdit()
        self.layout.addWidget(self.genres_label)
        self.layout.addWidget(self.genres_input)

        self.developer_label = QLabel('Developer:')
        self.developer_input = QLineEdit()
        self.layout.addWidget(self.developer_label)
        self.layout.addWidget(self.developer_input)

        button_layout = QHBoxLayout()
        self.add_button = QPushButton('Add Game')
        self.add_button.clicked.connect(self.add_game)
        button_layout.addWidget(self.add_button)

        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.close)
        button_layout.addWidget(self.cancel_button)

        self.layout.addLayout(button_layout)

    def add_game(self):
        game_data = {
            'title': self.title_input.text(),
            'platforms': [platform.strip() for platform in self.platforms_input.text().split(',')],
            'genres': [genre.strip() for genre in self.genres_input.text().split(',')],
            'developer': self.developer_input.text()
        }

        try:
            create_games(game_data)
            QMessageBox.information(self, 'Success', 'Game added successfully.')
            self.game_added.emit()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to add game: {str(e)}')
