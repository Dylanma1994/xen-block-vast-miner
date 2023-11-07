from PySide6.QtCore import QObject, Signal


class SignalBus(QObject):
    switchToSampleCard = Signal(str, int)
    micaEnableChanged = Signal(bool)
    supportSignal = Signal()

signalBus = SignalBus()