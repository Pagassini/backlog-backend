from PyQt5.QtWidgets import QHBoxLayout, QLabel, QComboBox, QWidget
import api

class UserSelectionWidget(QWidget):
    LABEL_TEXT = "Select User:"
    LABEL_STYLE = "color: white; font-size: 18px;"
    COMBOBOX_STYLE = "font-size: 16px;"

    def __init__(self):
        super().__init__()
        self.users = api.fetch_users()
        self.selected_user_id = None
        self._setup_ui()

    def _setup_ui(self):
        """Setup the UI components and layout."""
        self.layout = QHBoxLayout(self)

        self._add_user_label()
        self._add_user_combo()

    def _add_user_label(self):
        """Add the user selection label to the layout."""
        user_label = QLabel(self.LABEL_TEXT)
        user_label.setStyleSheet(self.LABEL_STYLE)
        self.layout.addWidget(user_label)

    def _add_user_combo(self):
        """Add the user selection combo box to the layout."""
        user_combo = QComboBox()
        user_combo.addItems([user['username'] for user in self.users])
        user_combo.setStyleSheet(self.COMBOBOX_STYLE)
        self.layout.addWidget(user_combo)
