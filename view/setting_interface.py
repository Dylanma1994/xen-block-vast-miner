from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget, QLabel
from qfluentwidgets import *

from common.config import cfg, HELP_URL, YEAR, AUTHOR, VERSION, FEEDBACK_URL
from common.style_sheet import StyleSheet


class SettingInterface(ScrollArea):

    # create widget and layout
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)

        # setting label
        self.settingLabel = QLabel(self.tr('Settings'), self)

        # Eth Address config
        self.ethGroup = SettingCardGroup(
            self.tr("Eth Config"), self.scrollWidget
        )
        self.ethCard = PushSettingCard(
            self.tr('ETH Address'),
            FluentIcon.PASTE,
            self.tr('MetaMask Address'),
            self.tr('content'),
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
            cfg.get(cfg.logFolder),
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
        self.__connectSignalToSlot()

    def __initLayout(self):
        self.settingLabel.move(36, 30)
        # add card to group
        self.ethGroup.addSettingCard(self.ethCard)
        self.sshGroup.addSettingCard(self.sshCard)
        self.logGroup.addSettingCards([self.logEnableCard, self.logFolderCard])
        self.personalGroup.addSettingCard(self.languageCard)
        self.aboutGroup.addSettingCards([self.helpCard, self.feedbackCard, self.aboutCard])

        # add group to layout
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.ethGroup)
        self.expandLayout.addWidget(self.sshGroup)
        self.expandLayout.addWidget(self.logGroup)
        self.expandLayout.addWidget(self.personalGroup)
        self.expandLayout.addWidget(self.aboutGroup)

    def __showRestartToolTip(self):
        InfoBar.success(
            self.tr('Updated successfully'),
            self.tr('Configuration takes effect after restart'),
            duration=1500,
            parent=self
        )

    def __connectSignalToSlot(self):
        # restart
        cfg.appRestartSig.connect(self.__showRestartToolTip)
        self.feedbackCard.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(FEEDBACK_URL))
        )