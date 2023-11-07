from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, QColor, QBrush
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from qfluentwidgets import ScrollArea, isDarkTheme

from common.style_sheet import StyleSheet
from components.link_card import LinkCardView
from common.config import HELP_URL, cfg
from components.sample_card import SampleCardView


class BannerWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(336)

        self.vBoxLayout = QVBoxLayout(self)
        self.appLabel = QLabel('XenBlocks Vast Miner', self)
        self.banner = QPixmap(f"{cfg.imagePath}/header1.png")
        self.linkCardView = LinkCardView(self)

        self.appLabel.setObjectName('appLabel')

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(0, 20, 0, 0)
        self.vBoxLayout.addWidget(self.appLabel)
        self.vBoxLayout.addWidget(self.linkCardView, 1, Qt.AlignmentFlag.AlignBottom)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.linkCardView.addCard(
            f"{cfg.imagePath}/logo.png",
            self.tr('Getting Started'),
            self.tr('An overview of app development options and samples.'),
            HELP_URL
        )

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.RenderHint.SmoothPixmapTransform | QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)

        path = QPainterPath()
        path.setFillRule(Qt.FillRule.WindingFill)
        w, h = self.width(), 200
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h-50, 50, 50))
        path.addRect(QRectF(w-50, 0, 50, 50))
        path.addRect(QRectF(w-50, h-50, 50, 50))
        path = path.simplified()

        # draw background color
        if not isDarkTheme():
            painter.fillPath(path, QColor(206, 216, 228))
        else:
            painter.fillPath(path, QColor(0, 0, 0))

        # draw banner image
        pixmap = self.banner.scaled(
            self.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        path.addRect(QRectF(0, h, w, self.height() - h))
        painter.fillPath(path, QBrush(pixmap))

class HomeInterface(ScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = BannerWidget(self)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.__initWidget()
        self.loadSamples()

    def __initWidget(self):
        self.view.setObjectName('view')
        self.setObjectName('homeInterface')
        StyleSheet.HOME_INTERFACE.apply(self)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

    def loadSamples(self):
        basicInputView = SampleCardView(
            self.tr("Basic samples"), self.view)
        self.vBoxLayout.addWidget(basicInputView)