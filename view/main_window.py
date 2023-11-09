from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QDesktopServices, QIcon
from PySide6.QtWidgets import QApplication

from common.signal_bus import signalBus
from qfluentwidgets import FluentIcon as FIF, NavigationItemPosition, SplashScreen, NavigationAvatarWidget
from qfluentwidgets import FluentWindow, MessageBox

from common.translator import Translator
from view.home_interface import HomeInterface
from view.setting_interface import SettingInterface
from common.config import SUPPORT_URL, cfg


class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()

        # create sub interface
        self.homeInterface = HomeInterface(self)
        self.settingInterface = SettingInterface(self)

        # enable acrylic effect
        self.navigationInterface.setAcrylicEnabled(True)

        self.connectSingnalToSlot()

        # add items to navigation interface
        self.initNavigation()
        self.splashScreen.finish()

    def initWindow(self):
        self.resize(960, 780)
        self.setMinimumWidth(760)
        self.setWindowIcon(QIcon(f"{cfg.imagePath}/logo.png"))
        self.setWindowTitle('Miner XenBlocks On Vast')

        self.setMicaEffectEnabled(cfg.get(cfg.micaEnabled))

        # todo create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.show()
        QApplication.processEvents()

    def connectSingnalToSlot(self):
        signalBus.micaEnableChanged.connect(self.setMicaEffectEnabled)
        # signalBus.switchToSampleCard.connect(self.switchToSample)
        signalBus.supportSignal.connect(self.onSupport)

    def initNavigation(self):
        t = Translator()
        self.addSubInterface(self.homeInterface, FIF.HOME, self.tr('Home'))
        self.navigationInterface.addSeparator()

        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('dylan', f"{cfg.imagePath}/logo.png"),
            onClick=self.onSupport,
            position=NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(self.settingInterface, FIF.SETTING, self.tr('Setting'), NavigationItemPosition.BOTTOM)

    def onSupport(self):
        w = MessageBox(
            '支持作者',
            '个人开发不易, 如果这个项目帮助到了您，请考虑请作者喝一杯咖啡',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')
        if w.exec():
            QDesktopServices.openUrl(QUrl(SUPPORT_URL))
