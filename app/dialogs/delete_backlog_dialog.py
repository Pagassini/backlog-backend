from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox

class DeleteBacklogDialog(QDialog):
    BACKGROUND_COLOR = "#2e2e2e"
    TEXT_COLOR = "white"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle('Confirm Deletion')
        self.setStyleSheet(f"background-color: {self.BACKGROUND_COLOR}; color: {self.TEXT_COLOR};")

        self.layout = QVBoxLayout(self)

        self._add_label()
        self._add_button_box()

    def _add_label(self):
        label = QLabel('Are you sure you want to delete this backlog?')
        self.layout.addWidget(label)

    def _add_button_box(self):
        button_box = QDialogButtonBox(QDialogButtonBox.Yes | QDialogButtonBox.No)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)
