from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

class BacklogTable(QTableWidget):
    COLUMN_HEADERS = ['Game', 'Status']
    COLUMN_COUNT = 2

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_table()

    def _setup_table(self):
        self.setColumnCount(self.COLUMN_COUNT)
        self.setHorizontalHeaderLabels(self.COLUMN_HEADERS)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def load_backlogs(self, backlogs):
        self.setRowCount(len(backlogs))
        for row_num, backlog in enumerate(backlogs):
            self._add_backlog_to_row(row_num, backlog)

    def _add_backlog_to_row(self, row_num, backlog):
        item_game = self._create_table_item(backlog['_id'])
        item_game.setData(Qt.UserRole, backlog['_id'])
        self.setItem(row_num, 0, item_game)

        item_status = self._create_table_item(backlog['status'])
        self.setItem(row_num, 1, item_status)

    def _create_table_item(self, text):
        item = QTableWidgetItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        return item

    def current_backlog(self):
        current_row = self.currentRow()
        if current_row == -1:
            return None

        return {
            '_id': self.item(current_row, 0).data(Qt.UserRole),
            'status': self.item(current_row, 1).text()
        }

