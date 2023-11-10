from typing import Union

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QPushButton
from qfluentwidgets import SettingCard, FluentIconBase, PasswordLineEdit


class PasswordLineEditSettingCard(SettingCard):

    clicked = Signal()
    def __init__(self, text, icon: Union[str, QIcon, FluentIconBase], title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.text = PasswordLineEdit(self)
        self.button = QPushButton(text, self)
        self.hBoxLayout.addWidget(self.text, 0, Qt.AlignmentFlag.AlignRight)
        self.hBoxLayout.addSpacing(16)
        self.button.clicked.connect(self.clicked)
