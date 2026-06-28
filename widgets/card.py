from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class DashboardCard(QFrame):

    def __init__(self, title: str, value: str):
        super().__init__()

        self.setObjectName("Card")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            color:#AEB6C2;
            font-size:12pt;
        """)

        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        value_label.setStyleSheet("""
            color:white;
            font-size:28pt;
            font-weight:bold;
        """)

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addStretch()