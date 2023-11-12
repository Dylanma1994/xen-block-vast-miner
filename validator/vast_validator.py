from qfluentwidgets import ConfigValidator
from vast import VastClient


class VastValidator(ConfigValidator):

    def validate(self, value):
        if not value:
            return
        client = VastClient(value)
        client.test_api_connection()
        print("vast validate")
