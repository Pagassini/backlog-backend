from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from api.games import fetch_games_by_id

class BacklogTable(QTableWidget):
    COLUMN_HEADERS = ['Game', 'Status']
    COLUMN_COUNT = 2

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_table()

    def _setup_table(self):
        """Setup the table properties and headers."""
        self.setColumnCount(self.COLUMN_COUNT)
        self.setHorizontalHeaderLabels(self.COLUMN_HEADERS)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def load_backlogs(self, backlogs):
        """Load backlogs into the table."""
        self.setRowCount(len(backlogs))
        for row_num, backlog in enumerate(backlogs):
            game = fetch_games_by_id(backlog['game_id'])
            backlog['game_title'] = game['title']
            self._add_backlog_to_row(row_num, backlog)

    def _add_backlog_to_row(self, row_num, backlog):
        """Add a single backlog entry to a specified row."""
        item_game = self._create_table_item(backlog['game_title'])
        item_game.setData(Qt.UserRole, backlog['_id'])
        self.setItem(row_num, 0, item_game)

        item_status = self._create_table_item(backlog['status'])
        self.setItem(row_num, 1, item_status)
        self._apply_status_color(item_status, backlog['status'])

    def _create_table_item(self, text):
        """Create a table item with specified text and set it to be non-editable."""
        item = QTableWidgetItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        item.setTextAlignment(Qt.AlignCenter)  # Centraliza o texto
        return item

    def _apply_status_color(self, item, status):
        """Apply text color based on status value."""
        color_map = {
            'playing': QColor(180, 180, 0),    # Amarelo escuro
            'finished': QColor(0, 0, 180),     # Azul escuro
            'dropped': QColor(180, 0, 0),      # Vermelho escuro
            'completed': QColor(0, 180, 0)     # Verde escuro
        }
        if status in color_map:
            item.setForeground(color_map[status])

    def current_backlog(self):
        """Return the currently selected backlog entry."""
        current_row = self.currentRow()
        if current_row == -1:
            return None

        return {
            '_id': self.item(current_row, 0).data(Qt.UserRole),
            'status': self.item(current_row, 1).text()
        }

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.clearSelection()

