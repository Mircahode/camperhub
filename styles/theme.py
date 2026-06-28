COLORS = {
    "background": "#171A21",
    "sidebar": "#1C2028",
    "card": "#21252D",
    "primary": "#2F80ED",
    "success": "#2ECC71",
    "warning": "#F39C12",
    "danger": "#E74C3C",
    "text": "#FFFFFF",
    "text_secondary": "#AEB6C2",
    "border": "#2B313D",
}


STYLE = f"""
QMainWindow {{
    background: {COLORS["background"]};
}}

QWidget {{
    background: {COLORS["background"]};
    color: {COLORS["text"]};
    font-family: Segoe UI;
    font-size: 11pt;
}}

QFrame#Sidebar {{
    background: {COLORS["sidebar"]};
    border-right: 1px solid {COLORS["border"]};
}}

QFrame#Card {{
    background: {COLORS["card"]};
    border: 1px solid {COLORS["border"]};
    border-radius: 14px;
}}

QPushButton {{
    background: {COLORS["primary"]};
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: bold;
}}

QPushButton:hover {{
    background: #4A95F5;
}}

QListWidget {{
    background: transparent;
    border: none;
}}

QListWidget::item {{
    padding: 12px;
    border-radius: 8px;
}}

QListWidget::item:selected {{
    background: {COLORS["primary"]};
}}

QLabel#Title {{
    font-size: 28pt;
    font-weight: bold;
}}

QLabel#SubTitle {{
    color: {COLORS["text_secondary"]};
    font-size: 12pt;
}}
"""