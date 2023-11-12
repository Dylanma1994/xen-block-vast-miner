from pathlib import Path

from qfluentwidgets import ConfigValidator


class FilePathValidator(ConfigValidator):

    def validate(self, value):
        return Path(value).exists()

    def correct(self, value):
        if Path(value).exists():
            return value
        else: return None