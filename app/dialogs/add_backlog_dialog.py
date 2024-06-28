from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QDialogButtonBox
from PyQt5.QtCore import Qt

class AddBacklogDialog(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Backlog')
        self.setStyleSheet("background-color: #2e2e2e; color: white;")  # Definindo o fundo preto e texto branco
        self.layout = QVBoxLayout(self)

        self.game_id_label = QLabel('Game ID:')
        self.game_id_input = QLineEdit('', self)  # Campo para inserir o game_id
        self.layout.addWidget(self.game_id_label)
        self.layout.addWidget(self.game_id_input)

        self.status_label = QLabel('Status:')
        self.status_input = QComboBox(self)
        self.status_input.addItems(['finished', 'playing', 'dropped', 'completed'])
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.status_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

        self.user_id = user_id  # Armazenando o user_id recebido como parâmetro

    def get_data(self):
        game_id = self.game_id_input.text()
        status = self.status_input.currentText()
        return {
            'game_id': game_id,
            'user_id': self.user_id,
            'status': status
        }