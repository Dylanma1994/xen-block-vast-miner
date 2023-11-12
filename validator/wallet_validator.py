import re

from qfluentwidgets import ConfigValidator
from web3 import Web3


class WalletAddressValidator(ConfigValidator):

    def validate(self, value):
        if value:
            return (re.match("^0x[0-9a-fA-F]{40}$", value)
                and value == Web3.to_checksum_address(value))
        return False

    def correct(self, value):
        if self.validate(value):
            return value
        else: return ''