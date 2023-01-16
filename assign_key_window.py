from typing import List

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from pynput_robocorp import keyboard


class AssignHotKey(QWidget):
    closed = Signal(QWidget, int, list)

    def __init__(self, parent=None, index: int = 0):
        super().__init__(None)
        self.show()
        self.launch_window = parent
        self.index = index
        self.pressed_keys = []
        self.vertical_layout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.load_ui()
        self.listener = keyboard.Listener(on_press=self.press_keys,
                                          supress=True)
        self.listener.start()

    def load_ui(self):
        self.label.setFont("Verdana, 25")
        self.label.setScaledContents(True)
        h_layout = QHBoxLayout()
        finish_button = QPushButton("Accept")
        clear_button = QPushButton("Clear")
        cancel_button = QPushButton("Cancel")

        finish_button.clicked.connect(lambda: self.assign(True))
        cancel_button.clicked.connect(lambda: self.assign(False))
        clear_button.clicked.connect(self.clear)
        for widget in finish_button, clear_button, cancel_button:
            h_layout.addWidget(widget)
        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addLayout(h_layout)
        self.setLayout(self.vertical_layout)

    def assign(self, to_assign: bool):
        if to_assign:
            self.closed.emit(self, self.index, self.parse_input())
        else:
            self.closed.emit(self, self.index, [])
        self.close()

    def clear(self):
        self.pressed_keys.clear()
        self.deploy_keys()

    def parse_input(self) -> List[str]:
        without_quot = [x.replace("'", "").lower() for x in self.pressed_keys]
        without_key_dot = [x.replace("key.", "") for x in without_quot]
        return without_key_dot

    def deploy_keys(self):
        self.label.setText("+".join(self.pressed_keys))
        self.label.adjustSize()

    def press_keys(self, key: keyboard.KeyCode):
        key = str(key)
        key = key.replace("_l", "")
        if key not in self.pressed_keys:

            self.pressed_keys.append(key)
            self.deploy_keys()
        else:
            self.pressed_keys.remove(key)
            self.deploy_keys()

    def closeEvent(self, event) -> None:
        self.stop()

    def stop(self):
        self.listener.stop()
