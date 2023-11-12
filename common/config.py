import sys, os, re
from enum import Enum

from PySide6.QtCore import QLocale
from qfluentwidgets import ConfigSerializer, QConfig, ConfigItem, FolderValidator, BoolValidator, \
    OptionsConfigItem, OptionsValidator, RangeValidator, RangeConfigItem, Theme, qconfig, ConfigValidator

from validator import WalletAddressValidator, VastValidator, FilePathValidator


class Language(Enum):
    CHINESE_SIMPLIFIED = QLocale(QLocale.Language.Chinese, QLocale.Country.China)
    ENGLISH = QLocale(QLocale.Language.English)
    AUTO = QLocale()


class LanguageSerializer(ConfigSerializer):
    """ Language serializer """

    def serialize(self, language):
        return language.value.name() if language != Language.AUTO else "Auto"

    def deserialize(self, value: str):
        return Language(QLocale(value)) if value != "Auto" else Language.AUTO


def isWin11():
    return sys.platform == 'win32' and sys.getwindowsversion().build >= 22000


class Config(QConfig):
    """ Config of application """

    # static config
    projectPath = os.path.abspath(os.path.dirname(__file__)) + '/..'
    qssPath = projectPath + '/resources/qss'
    imagePath = projectPath + '/resources/images'

    # app confit
    wallet = ConfigItem("Wallet", "Address", '', WalletAddressValidator())
    vast = ConfigItem("Vast", "ApiKey", '', VastValidator())
    sshPrivateKeyFile = ConfigItem("SSH", "PrivateKeyFilePath", '', FilePathValidator())
    logEnable = ConfigItem("Log", "LogEnabled", False, BoolValidator())
    logFolder = ConfigItem("Log", "LogFolder", './', FolderValidator())

    # main window
    micaEnabled = ConfigItem("MainWindow", "MicaEnabled", isWin11(), BoolValidator())
    dpiScale = OptionsConfigItem(
        "MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]), restart=True)
    language = OptionsConfigItem(
        "MainWindow", "Language", Language.AUTO, OptionsValidator(Language), LanguageSerializer(), restart=True)

    # Material
    blurRadius = RangeConfigItem("Material", "AcrylicBlurRadius", 15, RangeValidator(0, 40))

    # software update
    checkUpdateAtStartUp = ConfigItem("Update", "CheckUpdateAtStartUp", True, BoolValidator())


YEAR = 2023
AUTHOR = "Dylan"
HELP_URL = "https://qfluentwidgets.com"
REPO_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets"
FEEDBACK_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/issues"
RELEASE_URL = "https://github.com/zhiyiYo/PyQt-Fluent-Widgets/releases/latest"
SUPPORT_URL = "https://afdian.net/a/zhiyiYo"
VERSION = "v0.1"

cfg = Config()
cfg.themeMode.value = Theme.AUTO
qconfig.load('app/config/config.json', cfg)

print(cfg.toDict())