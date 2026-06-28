from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout

from widgets.card import DashboardCard


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        title = QLabel("Dashboard")
        title.setObjectName("Title")

        subtitle = QLabel("Oversikt over bobilutleien")
        subtitle.setObjectName("SubTitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        grid = QGridLayout()
        grid.setSpacing(20)

        grid.addWidget(DashboardCard("Omsetning", "0 kr"), 0, 0)
        grid.addWidget(DashboardCard("Bookinger", "0"), 0, 1)
        grid.addWidget(DashboardCard("Belegg", "0 %"), 1, 0)
        grid.addWidget(DashboardCard("Ledige uker", "23"), 1, 1)

        layout.addLayout(grid)
        layout.addStretch()