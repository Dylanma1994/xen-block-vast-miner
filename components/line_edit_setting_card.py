from typing import Union

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon, Qt
from qfluentwidgets import SettingCard, FluentIconBase, LineEdit, PrimaryPushButton, InfoBar



class LineEditSettingCard(SettingCard):

    save = Signal(str)

    def __init__(self, text: str, icon: Union[str, QIcon, FluentIconBase], title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.text = LineEdit(self)
        self.text.setText(text)
        self.button = PrimaryPushButton(self)
        self.button.setText(self.tr("Save"))
        self.hBoxLayout.addWidget(self.text, 1, Qt.AlignmentFlag.AlignRight)
        self.hBoxLayout.addSpacing(8)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignRight)
        self.hBoxLayout.addSpacing(16)

        self.button.clicked.connect(self._save)

    def _save(self):
        print("save")
        self.save.emit(self.text.text())
