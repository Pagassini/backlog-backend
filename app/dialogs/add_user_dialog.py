from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox

class AddUserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add User')
        self.layout = QVBoxLayout(self)

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit(self)
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit(self)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, parent=self)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

    def get_data(self):
        return {
            'username': self.username_input.text(),
            'email': self.email_input.text(),
            'password': self.password_input.text()
        }