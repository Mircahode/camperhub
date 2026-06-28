from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QWidget,
)

from pages.dashboard import DashboardPage
from widgets.sidebar import Sidebar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RentalOS")
        self.resize(1400, 900)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = Sidebar()

        self.stack = QStackedWidget()
        self.dashboard = DashboardPage()
        self.stack.addWidget(self.dashboard)

        self.sidebar.menu.currentRowChanged.connect(self.change_page)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

    def change_page(self, index: int):
        if index < self.stack.count():
            self.stack.setCurrentIndex(index)