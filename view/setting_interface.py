import re

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget, QLabel
from qfluentwidgets import *
from web3 import Web3

from common.config import cfg, HELP_URL, YEAR, AUTHOR, VERSION, FEEDBACK_URL
from common.style_sheet import StyleSheet
from components import FileSettingCard, LineEditSettingCard
from vast import VastClient


class SettingInterface(ScrollArea):

    # create widget and layout
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)

        # setting label
        self.settingLabel = QLabel(self.tr('Settings'), self)

        # wallet address config
        self.walletGroup = SettingCardGroup(
            self.tr("Wallet Config"), self.scrollWidget
        )
        self.walletAddressCard = LineEditSettingCard(
            cfg.wallet.value,
            FluentIcon.PASTE,
            self.tr('Address'),
            self.tr('Pls copy metamask wallet address to here!'),
            self.walletGroup
        )

        # vast config
        self.vastGroup = SettingCardGroup(
            self.tr("Vast Config"), self.scrollWidget
        )
        self.vastApiKeyCard = LineEditSettingCard(
            cfg.vast.value,
            FluentIcon.PASTE,
            self.tr('Vast Api Key'),
            self.tr('Pls copy vast api key to here!'),
            self.vastGroup
        )
        self.sshPrivateKeyFileCard = FileSettingCard(
            cfg.sshPrivateKeyFile,
            self.tr("Vast SSH Private Key File Path"),
            self.tr("Please Choose File"),
            buttonText=cfg.sshPrivateKeyFile.value if cfg.sshPrivateKeyFile else self.tr("Choose file"),
            parent=self.vastGroup
        )

        # log config
        self.logGroup = SettingCardGroup(
            self.tr("Log Config"), self.scrollWidget
        )
        self.logEnableCard = SwitchSettingCard(
            FluentIcon.TRANSPARENT,
            self.tr("Log Enable"),
            self.tr("Enable will record log in log directory"),
            cfg.micaEnabled,
            self.logGroup
        )
        self.logFolderCard = PushSettingCard(
            self.tr("Choose folder"),
            FluentIcon.DOWNLOAD,
            self.tr("Log directory"),
            cfg.logFolder.value if cfg.logFolder else self.tr("Please log file save directory"),
            self.logGroup
        )

        # personal Group
        self.personalGroup = SettingCardGroup(
            self.tr('Personalization'), self.scrollWidget
        )
        self.languageCard = ComboBoxSettingCard(
            cfg.language,
            FluentIcon.LANGUAGE,
            self.tr("Language"),
            self.tr("Set your preferred language for UI"),
            texts=["简体中文", "English", self.tr("Use system setting")],
            parent=self.personalGroup
        )

        # application
        self.aboutGroup = SettingCardGroup(self.tr('About'), self.scrollWidget)
        self.helpCard = HyperlinkCard(
            HELP_URL,
            self.tr('Open help page'),
            FluentIcon.HELP,
            self.tr('Help'),
            self.tr(
                'Discover new features and learn useful tips about PyQt-Fluent-Widgets'),
            self.aboutGroup
        )
        self.feedbackCard = PrimaryPushSettingCard(
            self.tr('Provide feedback'),
            FluentIcon.FEEDBACK,
            self.tr('Provide feedback'),
            self.tr('Help us improve PyQt-Fluent-Widgets by providing feedback'),
            self.aboutGroup
        )
        self.aboutCard = PrimaryPushSettingCard(
            self.tr('Check update'),
            FluentIcon.INFO,
            self.tr('About'),
            '© ' + self.tr('Copyright') + f" {YEAR}, {AUTHOR}. " +
            self.tr('Version') + " " + VERSION,
            self.aboutGroup
        )

        self.__initWidget()

    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 80, 0, 20)
        # set widget
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')

        self.scrollWidget.setObjectName('scrollWidget')
        self.settingLabel.setObjectName('settingLabel')
        StyleSheet.SETTING_INTERFACE.apply(self)

        self.__initLayout()
        self._connect_signal_to_slot()

    def __initLayout(self):
        self.settingLabel.move(36, 30)
        # add card to group
        self.walletGroup.addSettingCard(self.walletAddressCard)
        self.vastGroup.addSettingCard(self.sshPrivateKeyFileCard)
        self.vastGroup.addSettingCard(self.vastApiKeyCard)
        self.logGroup.addSettingCards([self.logEnableCard, self.logFolderCard])
        self.personalGroup.addSettingCard(self.languageCard)
        self.aboutGroup.addSettingCards([self.helpCard, self.feedbackCard, self.aboutCard])

        # add group to layout
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.walletGroup)
        self.expandLayout.addWidget(self.vastGroup)
        self.expandLayout.addWidget(self.logGroup)
        self.expandLayout.addWidget(self.personalGroup)
        self.expandLayout.addWidget(self.aboutGroup)

    def _show_restart_tool_tip(self):
        InfoBar.success(
            self.tr('Updated successfully'),
            self.tr('Configuration takes effect after restart'),
            duration=1500,
            parent=self
        )

    def _check_address(self, address: bool):
        res = (re.match("^0x[0-9a-fA-F]{40}$", address)
               and address == Web3.to_checksum_address(address))
        if res:
            cfg.set(cfg.wallet, address)
            self.walletAddressCard.text.setText(address)
        if res:
            InfoBar.success(
                self.tr('Address check successfully'),
                self.tr('Address follows EIP-55 checksum encoding'),
                duration=1500,
                parent=self
            )
        else:
            InfoBar.error(
                self.tr('Address check failed'),
                self.tr('Address not follows EIP-55 checksum encoding'),
                duration=1500,
                parent=self
            )

    def _check_api_key(self, api_key: str):
        client = VastClient(api_key)
        res = client.test_api_connection()
        if res["status"]:
            cfg.set(cfg.vast, api_key)
            InfoBar.success(
                self.tr('Save successfully'),
                self.tr('Test connection successfully'),
                duration=1500,
                parent=self
            )
        else:
            InfoBar.error(
                self.tr('Save failed'),
                self.tr('Test connection failed'),
                duration=1500,
                parent=self
            )

    def _show_ssh_file_path(self, file_path: str):
        self.sshPrivateKeyFileCard.setContent(file_path)
        self.sshPrivateKeyFileCard.button.setText(file_path)

    def _connect_signal_to_slot(self):
        cfg.appRestartSig.connect(self._show_restart_tool_tip)
        self.walletAddressCard.save.connect(self._check_address)
        self.vastApiKeyCard.save.connect(self._check_api_key)
        self.sshPrivateKeyFileCard.fileChanged.connect(self._show_ssh_file_path)
        self.feedbackCard.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(FEEDBACK_URL))
        )
