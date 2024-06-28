import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, 
    QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QInputDialog, 
    QMessageBox, QComboBox, QLabel, QDialog, QDialogButtonBox, QLineEdit
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

import api
from dialogs.update_backlog_dialog import UpdateBacklogDialog
from dialogs.add_backlog_dialog import AddBacklogDialog

class GameLibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Backlog Manager')
        self.setGeometry(100, 100, 1000, 800)  # Aumentando o tamanho da janela
        self.set_dark_theme()
        self.initUI()

    def set_dark_theme(self):
        self.setStyleSheet(
            "QLineEdit, QComboBox, QTableWidget, QPushButton, QLabel { color: white; background-color: #2e2e2e; border: 2px solid #444; border-radius: 10px; } "
            "QPushButton:hover { background-color: #444; }"
        )

    def initUI(self):
        self.users = api.fetch_users()
        self.selected_user_id = None

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.user_layout = QHBoxLayout()
        self.user_label = QLabel("Select User:")
        self.user_label.setStyleSheet("color: white; font-size: 18px;")  # Aumentando o tamanho da fonte
        self.user_combo = QComboBox()
        self.user_combo.addItems([user['username'] for user in self.users])
        self.user_combo.currentIndexChanged.connect(self.load_user_backlogs)
        self.user_combo.setStyleSheet("font-size: 16px;")  # Aumentando o tamanho da fonte do combo box
        self.user_layout.addWidget(self.user_label)
        self.user_layout.addWidget(self.user_combo)

        self.layout.addLayout(self.user_layout)

        self.table = QTableWidget()
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)  # Impedir edição na tabela
        self.table.setSelectionBehavior(QTableWidget.SelectRows)  # Selecionar linhas inteiras
        self.table.setStyleSheet("font-size: 16px; background-color: #2e2e2e; color: white;")  # Aumentando o tamanho da fonte da tabela e definindo o fundo preto
        self.layout.addWidget(self.table)

        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Backlog")
        self.add_button.clicked.connect(self.add_backlog)
        self.add_button.setStyleSheet("background-color: #007BFF; color: white; font-size: 20px; padding: 12px 24px; border-radius: 10px;")
        self.update_button = QPushButton("Update Backlog")
        self.update_button.clicked.connect(self.update_backlog)
        self.update_button.setStyleSheet("background-color: #28A745; color: white; font-size: 20px; padding: 12px 24px; border-radius: 10px;")
        self.delete_button = QPushButton("Delete Backlog")
        self.delete_button.clicked.connect(self.delete_backlog)
        self.delete_button.setStyleSheet("background-color: #DC3545; color: white; font-size: 20px; padding: 12px 24px; border-radius: 10px;")
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.button_layout)

        self.load_user_backlogs()

    def load_user_backlogs(self):
        user_index = self.user_combo.currentIndex()
        self.selected_user_id = self.users[user_index]['_id']
        backlogs = api.fetch_backlogs(self.selected_user_id)

        self.table.setRowCount(len(backlogs))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Game ID', 'User ID', 'Status'])

        for row_num, backlog in enumerate(backlogs):
            item_id = QTableWidgetItem(backlog['_id'])  # Usando o _id do backlog
            item_id.setData(Qt.UserRole, backlog['_id'])  # Armazenando _id do backlog no UserRole
            self.table.setItem(row_num, 0, item_id)
            self.table.setItem(row_num, 1, QTableWidgetItem(backlog['user_id']))

            status_item = QTableWidgetItem(backlog['status'])
            status_item.setBackground(self.get_status_color(backlog['status']))
            self.table.setItem(row_num, 2, status_item)

    def get_status_color(self, status):
        if status == 'finished':
            return QColor(Qt.green)
        elif status == 'playing':
            return QColor(Qt.blue)
        elif status == 'dropped':
            return QColor(Qt.red)
        elif status == 'completed':
            return QColor(Qt.gray)

    def add_backlog(self):
            dialog = AddBacklogDialog(self.selected_user_id, self)
            dialog.setStyleSheet("background-color: #2e2e2e; color: white;")  # Definindo o fundo preto e texto branco para a janela de diálogo
            if dialog.exec_():
                backlog_data = dialog.get_data()
                if not backlog_data['game_id'] or not backlog_data['status']:
                    self.show_error("Game ID and Status fields are required!")
                    return

                api.create_backlog(backlog_data)
                self.load_user_backlogs()

    def update_backlog(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            self.show_error("No backlog selected!")
            return

        item_id = self.table.item(selected_row, 0)
        if item_id is None:
            self.show_error("No backlog selected!")
            return

        backlog_id = item_id.data(Qt.UserRole)  # Usando _id do backlog armazenado no UserRole
        current_status = self.table.item(selected_row, 2).text()  # Obtendo o status atual do backlog
        dialog = UpdateBacklogDialog(current_status, self)
        dialog.setStyleSheet("background-color: #2e2e2e; color: white;")  # Definindo o fundo preto e texto branco para a janela de diálogo
        if dialog.exec_():
            data = dialog.get_data()
            if 'status' not in data:
                self.show_error("Status field is required!")
                return

            updated_backlog = {
                'status': data['status']
            }
            api.update_backlog(backlog_id, updated_backlog)
            self.load_user_backlogs()

    def delete_backlog(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            self.show_error("No backlog selected!")
            return

        item_id = self.table.item(selected_row, 0)
        if item_id is None:
            self.show_error("No backlog selected!")
            return

        backlog_id = item_id.data(Qt.UserRole)  # Usando _id do backlog armazenado no UserRole
        api.delete_backlog(backlog_id)
        self.load_user_backlogs()

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameLibraryApp()
    window.show()
    sys.exit(app.exec_())
