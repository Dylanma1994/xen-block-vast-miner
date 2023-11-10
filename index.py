# coding: utf-8
import os
import sys

from PySide6.QtCore import QTranslator
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentTranslator

from common.config import cfg
from view.main_window import MainWindow

# enable dpi scale
if cfg.get(cfg.dpiScale) != "Auto":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
    os.environ["QT_SCALE_FACTOR"] = str(cfg.get(cfg.dpiScale))

# create application
app = QApplication(sys.argv)

# i18n
locale = cfg.get(cfg.language).value
translator = FluentTranslator(locale)
appTranslator = QTranslator()
appTranslator.load(locale, "", "", "resources/i18n")

app.installTranslator(translator)
app.installTranslator(appTranslator)

# create main window
w = MainWindow()
w.show()

app.exec()