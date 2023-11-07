from enum import Enum
from common.config import cfg

from qfluentwidgets import StyleSheetBase, Theme, qconfig


class StyleSheet(StyleSheetBase, Enum):
    LINK_CARD = "link_card"
    HOME_INTERFACE = 'home_interface'
    SETTING_INTERFACE = 'setting_interface'
    SAMPLE_CARD = 'sample_card'

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"{cfg.qssPath}/{theme.value.lower()}/{self.value}.qss"