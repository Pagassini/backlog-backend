import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QMessageBox, QPushButton, QSizePolicy
from PyQt5.QtGui import QIcon
from api.user import delete_user, fetch_users, create_user
from api.backlog import fetch_backlogs, create_backlog, update_backlog, delete_backlog
from api.games import fetch_games, fetch_games_by_id
from dialogs.add_user_dialog import AddUserDialog
from dialogs.add_backlog_dialog import AddBacklogDialog
from dialogs.update_backlog_dialog import UpdateBacklogDialog
from dialogs.delete_backlog_dialog import DeleteBacklogDialog
from ui.buttons import AddBacklogButton, UpdateBacklogButton, DeleteBacklogButton
from ui.backlog_table import BacklogTable

class MainWindow(QMainWindow):
    WINDOW_TITLE = 'Backlog Manager'
    WINDOW_GEOMETRY = (100, 100, 1000, 800)
    ICONS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icons")
    STYLESHEET_FILE = "styles.qss"

    def __init__(self):
        super().__init__()
        self._setup_ui()
        self.load_users()

    def _setup_ui(self):
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setGeometry(*self.WINDOW_GEOMETRY)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self._add_user_combo_and_buttons()
        self._add_backlog_table()
        self._add_buttons()

    def _add_user_combo_and_buttons(self):
        user_layout = QHBoxLayout()
        
        self.user_combo = QComboBox()
        self.user_combo.currentIndexChanged.connect(self.load_backlogs)
        user_layout.addWidget(self.user_combo)
        
        self.add_user_button = self._create_button("Add.png", self.add_user)
        user_layout.addWidget(self.add_user_button)

        self.delete_user_button = self._create_button("Delete.png", self.delete_user)
        user_layout.addWidget(self.delete_user_button)
        
        self.layout.addLayout(user_layout)

    def _create_button(self, icon_filename, slot_function):
        button = QPushButton()
        icon_path = os.path.join(self.ICONS_PATH, icon_filename)
        button.setIcon(QIcon(icon_path))
        button.setFixedSize(30, 30)
        button.clicked.connect(slot_function)
        return button

    def _add_backlog_table(self):
        self.table = BacklogTable()
        self.layout.addWidget(self.table)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def _add_buttons(self):
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
        self.user_combo.clear()
        self.user_combo.addItems([user['username'] for user in self.users])

    def load_backlogs(self):
        user_index = self.user_combo.currentIndex()
        if user_index == -1:
            return
        self.selected_user_id = self.users[user_index]['_id']
        backlogs = fetch_backlogs(self.selected_user_id)
        
        for backlog in backlogs:
            game_id = backlog['game_id']
            game = fetch_games_by_id(game_id)
            backlog['game_title'] = game['title']  # Add the game title to the backlog

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

    def add_user(self):
        dialog = AddUserDialog(self)
        if dialog.exec_():
            data = dialog.get_data()
            create_user(data)
            self.load_users()

    def delete_user(self):
        user_index = self.user_combo.currentIndex()
        if user_index == -1:
            return
        
        user_id = self.users[user_index]['_id']
        delete_user(user_id)
        self.load_users()

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message)

def load_stylesheet(filename):
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stylesheet = load_stylesheet(MainWindow.STYLESHEET_FILE)
    app.setStyleSheet(stylesheet)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
