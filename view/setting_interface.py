from PySide6.QtCore import Qt, QSize, QStandardPaths
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import *

from common.config import cfg

class SettingInterface(ScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget(self)

        # setting label
        self.settingLabel = QLabel('Settings')

        # Eth Address config
        self.ethGroup = SettingCardGroup(
            self.tr("Eth Config"), self.scrollWidget
        )
        self.ethAddressCard = SettingCard()
        self.ethAddressCard = ComboBoxSettingCard(
            FluentIcon.TRANSPARENT,
            self.tr("ETH Address"),
            self.tr("Please copy MetaMask Address to here"),
            cfg.micaEnabled,
            self.ethGroup
        )

        # ssh config
        self.sshGroup = SettingCardGroup(
            self.tr("SSH Config"), self.scrollWidget
        )
        self.sshCard = FolderListSettingCard(
            cfg.sshFolder,
            self.tr("SSH Config"),
            directory='',
            parent=self.sshGroup
        )

        # log config
        self.logGroup = SettingCardGroup(
            self.tr("Log Config"), self.scrollWidget
        )
        self.ethAddressCard = SwitchSettingCard(
            FluentIcon.TRANSPARENT,
            self.tr("ETH Address"),
            self.tr("Please copy MetaMask Address to here"),
            cfg.micaEnabled,
            self.logGroup
        )
        self.logFolderCard = PushSettingCard(
            self.tr("Choose folder"),
            FluentIcon.DOWNLOAD,
            self.tr("Log directory"),
            cfg.get(cfg.downloadFolder),
            self.logGroup
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