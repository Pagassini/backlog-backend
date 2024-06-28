from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox

class UpdateBacklogDialog(QDialog):
    def __init__(self, current_status, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Update Backlog')
        self.setStyleSheet("background-color: #2e2e2e; color: white;")  # Definindo o fundo preto e texto branco
        self.layout = QVBoxLayout(self)

        self.status_label = QLabel('Status:')
        self.status_input = QComboBox(self)
        self.status_input.addItems(['finished', 'playing', 'dropped', 'completed'])
        self.status_input.setCurrentText(current_status)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.status_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

    def get_data(self):
        return {
            'status': self.status_input.currentText()
        }
