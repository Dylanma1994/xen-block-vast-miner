from PySide6.QtCore import Qt, QSize, QStandardPaths
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import (ScrollArea, PasswordLineEdit, SettingCardGroup, FolderListSettingCard, PushSettingCard,
                            FluentIcon as FIF)

from common.config import cfg

class SettingInterface(ScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget(self)

        # setting label
        self.settingLabel = QLabel('Settings')

        # eth address config
        self.ethAddress = PasswordLineEdit(self)
        self.ethAddress.setFixedSize(QSize())
        self.ethAddress.setPlaceholderText(self.tr("Enter your eth address"))

        # ssh private key file path
        self.sshGroup = SettingCardGroup(
            self.tr("SSH Privice Key"), self.scrollWidget
        )
        self.sshCard = FolderListSettingCard(
            cfg.sshFolder,
            self.tr("SSH Config"),
            directory='',
            parent=self.sshGroup
        )

        # download
        self.downloadFolderCard = PushSettingCard(
            self.tr("Choose folder"),
            FIF.DOWNLOAD,
            self.tr("Download directory"),
            cfg.get(cfg.downloadFolder),
            self.sshGroup
        )


        self.vBoxLayout = QVBoxLayout(self.view)

        self.__initWidget()

    def __initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('settingInterface')

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.textLabel)