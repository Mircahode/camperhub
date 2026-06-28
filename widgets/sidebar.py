from PySide6.QtWidgets import QFrame, QLabel, QListWidget, QVBoxLayout


class Sidebar(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("Sidebar")
        self.setFixedWidth(240)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        logo = QLabel("🚐 RentalOS")
        logo.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            color:white;
        """)

        self.menu = QListWidget()

        self.menu.addItems([
            "🏠 Dashboard",
            "📅 Kalender",
            "🚐 Bookinger",
            "👥 Kunder",
            "💰 Økonomi",
            "🔧 Vedlikehold",
            "⚙ Innstillinger",
        ])

        self.menu.setCurrentRow(0)

        layout.addWidget(logo)
        layout.addWidget(self.menu)
        layout.addStretch()