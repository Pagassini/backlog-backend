from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QComboBox, QMessageBox
from api.user import fetch_users
from api.backlog import fetch_backlogs, create_backlog, update_backlog, delete_backlog
from ui.buttons import AddBacklogButton, UpdateBacklogButton, DeleteBacklogButton
from ui.backlog_table import BacklogTable
from dialogs.add_backlog_dialog import AddBacklogDialog
from dialogs.update_backlog_dialog import UpdateBacklogDialog
from dialogs.delete_backlog_dialog import DeleteBacklogDialog

class MainWindow(QMainWindow):
    WINDOW_TITLE = 'Backlog Manager'
    WINDOW_GEOMETRY = (100, 100, 1000, 800)

    def __init__(self):
        super().__init__()
        self._setup_ui()
        self.load_users()

    def _setup_ui(self):
        """Setup the main window UI components and layout."""
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setGeometry(*self.WINDOW_GEOMETRY)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self._add_user_combo()
        self._add_backlog_table()
        self._add_buttons()

    def _add_user_combo(self):
        """Add user selection combo box to the layout."""
        self.user_combo = QComboBox()
        self.user_combo.currentIndexChanged.connect(self.load_backlogs)
        self.layout.addWidget(self.user_combo)

    def _add_backlog_table(self):
        """Add backlog table to the layout."""
        self.table = BacklogTable()
        self.layout.addWidget(self.table)

    def _add_buttons(self):
        """Add action buttons to the layout."""
        self.add_button = AddBacklogButton(self)
        self.add_button.clicked.connect(self.add_backlog)
        self.layout.addWidget(self.add_button)

        self.update_button = UpdateBacklogButton(self)
        self.update_button.clicked.connect(self.update_backlog)
        self.layout.addWidget(self.update_button)

        self.delete_button = DeleteBacklogButton(self)
        self.delete_button.clicked.connect(self.delete_backlog)
        self.layout.addWidget(self.delete_button)

    def load_users(self):
        self.users = fetch_users()
        self.user_combo.addItems([user['username'] for user in self.users])

    def load_backlogs(self):
        user_index = self.user_combo.currentIndex()
        self.selected_user_id = self.users[user_index]['_id']
        backlogs = fetch_backlogs(self.selected_user_id)
        self.table.load_backlogs(backlogs)

    def add_backlog(self):
        dialog = AddBacklogDialog(self.selected_user_id, self)
        if dialog.exec_():
            data = dialog.get_data()
            create_backlog(data)
            self.load_backlogs()

    def update_backlog(self):
        selected_backlog = self.table.current_backlog()
        if selected_backlog is None:
            self.show_error("No backlog selected!")
            return

        backlog_id = selected_backlog['_id']
        current_status = selected_backlog['status']

        dialog = UpdateBacklogDialog(current_status, self)
        if dialog.exec_():
            data = dialog.get_data()
            update_backlog(backlog_id, data)
            self.load_backlogs()

    def delete_backlog(self):
        selected_backlog = self.table.current_backlog()
        if selected_backlog is None:
            self.show_error("No backlog selected!")
            return

        backlog_id = selected_backlog['_id']

        dialog = DeleteBacklogDialog(self)
        if dialog.exec_():
            delete_backlog(backlog_id)
            self.load_backlogs()

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message)

