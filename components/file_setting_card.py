from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QFileDialog
from qfluentwidgets import SettingCard, ConfigItem, FluentIcon, PushButton
from common.config import cfg


class FileSettingCard(SettingCard):

    fileChanged = Signal(str)

    def __init__(self, configItem: ConfigItem, title: str, content: str = None, buttonText: str = None, directory = './', parent = None):
        super().__init__(FluentIcon.FOLDER, title, content, parent)
        self.configItem = configItem
        self._dialogDirectory = directory
        self.button = PushButton(buttonText or self.tr('Choose File'), self, FluentIcon.ADD)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignRight)
        self.hBoxLayout.addSpacing(16)
        self.button.clicked.connect(self._openFolder)

    def _openFolder(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, self.tr("Select File"))
        print(f"file path {file_path} {_}")
        if file_path:
            cfg.set(cfg.sshPrivateKeyFile, file_path)
            self.fileChanged.emit(file_path)
        else:
            print(f"file path not select")