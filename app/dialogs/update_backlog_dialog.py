from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QDialogButtonBox

class UpdateBacklogDialog(QDialog):
    BACKGROUND_COLOR = "#2e2e2e"
    TEXT_COLOR = "white"
    STATUS_OPTIONS = ['finished', 'playing', 'dropped', 'completed']

    def __init__(self, current_status, parent=None):
        super().__init__(parent)
        self._setup_ui(current_status)

    def _setup_ui(self, current_status):
        self.setWindowTitle('Update Backlog')
        self.setStyleSheet(f"background-color: {self.BACKGROUND_COLOR}; color: {self.TEXT_COLOR};")

        self.layout = QVBoxLayout(self)

        self._add_status_input(current_status)
        self._add_button_box()

    def _add_status_input(self, current_status):
        status_label = QLabel('Status:')
        self.status_input = QComboBox(self)
        self.status_input.addItems(self.STATUS_OPTIONS)
        self.status_input.setCurrentText(current_status)
        self.layout.addWidget(status_label)
        self.layout.addWidget(self.status_input)

    def _add_button_box(self):
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

    def get_data(self):
        return {
            'status': self.status_input.currentText()
        }
