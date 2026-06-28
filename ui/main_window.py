from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
)

from styles.theme import STYLE
from widgets.sidebar import Sidebar
from pages.dashboard import DashboardPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("RentalOS")
        self.resize(1600, 900)

        self.setStyleSheet(STYLE)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = Sidebar()
        self.dashboard = DashboardPage()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.dashboard)