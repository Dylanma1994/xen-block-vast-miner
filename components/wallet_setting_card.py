import re
from typing import Union
from web3 import Web3

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon, Qt
from qfluentwidgets import SettingCard, FluentIconBase, PasswordLineEdit, PrimaryPushButton, InfoBar

from common.config import cfg


class WalletAddressSettingCard(SettingCard):
    check = Signal(bool)

    def __init__(self, walletAddress: str, icon: Union[str, QIcon, FluentIconBase], title, content=None, parent=None):
        super().__init__(icon, title, content, parent)
        self.address = PasswordLineEdit(self)
        self.address.setText(walletAddress)
        self.button = PrimaryPushButton(self.tr("Confirm"), self)
        self.hBoxLayout.addWidget(self.address, 0, Qt.AlignmentFlag.AlignRight)
        self.hBoxLayout.addSpacing(8)
        self.hBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignRight)
        self.hBoxLayout.addSpacing(16)
        self.button.clicked.connect(self._check_address)

    def _check_address(self):
        address = self.address.text()
        res = (re.match("^0x[0-9a-fA-F]{40}$", address)
            and address == Web3.to_checksum_address(address))
        if res:
            cfg.set(cfg.wallet, address)

        self.check.emit(res)
