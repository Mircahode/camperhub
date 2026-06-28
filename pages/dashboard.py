from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout,
)

from widgets.card import DashboardCard


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)
        root.setContentsMargins(30, 30, 30, 30)
        root.setSpacing(25)

        title = QLabel("Dashboard")
        title.setObjectName("Title")

        subtitle = QLabel("Oversikt over virksomheten")
        subtitle.setObjectName("SubTitle")

        root.addWidget(title)
        root.addWidget(subtitle)

        cards = QGridLayout()
        cards.setSpacing(20)

        cards.addWidget(DashboardCard("Bobiler tilgjengelig", "18"), 0, 0)
        cards.addWidget(DashboardCard("Aktive bookinger", "7"), 0, 1)
        cards.addWidget(DashboardCard("Kunder", "246"), 1, 0)
        cards.addWidget(DashboardCard("Omsetning", "1,24 MNOK"), 1, 1)

        root.addLayout(cards)
        root.addStretch()