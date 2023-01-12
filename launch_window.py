from pathlib import Path
from typing import List

import PySide2
from PySide2 import QtCore
from PySide2.QtCore import QDir, Slot, Qt
from PySide2.QtWidgets import QFileDialog, QGridLayout

from generated_ui import Ui_Form
from defining_area import DefineAreaWindow, Area, QWidget, QApplication
from command_reader import HotKey, KeyMapper
from hotkeys_window import HotKeyWindow
import sys

from folder import Folder
from hotkey_processor import HotKeyProcessor
from default_struct import DefaultStruct


class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        main_layout = QGridLayout()
        self.setLayout(main_layout)


class LaunchWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.set_connections()
        self.defaults = DefaultStruct.from_file("defaults.json")
        self.load_default_value(self.defaults)
        self.keys = KeyMapper.from_file("keys.json")
        self.screenshot_area = Area()
        self.win: DefineAreaWindow = None
        self.hotkey_win: HotKeyWindow = None
        self.processor: HotKeyProcessor = None

    def load_default_value(self, struct: DefaultStruct):
        self.ui.path_input.setText(struct.default_path)
        self.ui.filename_input.setText(struct.default_image_name)
        self.ui.extension_input.setText(struct.default_image_ext)
        self.ui.backend_input.setCurrentText(struct.default_backend)

    def get_struct(self):
        return DefaultStruct(
            default_path=self.ui.path_input.text(),
            default_backend=self.ui.backend_input.currentText(),
            default_image_name=self.ui.filename_input.text(),
            default_image_ext=self.ui.extension_input.text(),
            default_is_paused=self.defaults.default_is_paused,
            default_after_screen_defining=self.defaults.default_after_screen_defining
        )

    def set_connections(self):
        self.ui.launch_button.clicked.connect(self.launch_button_click)
        self.ui.hotkey_button.clicked.connect(self.hotkey_button_click)
        self.ui.browse_button.clicked.connect(self.browse_button_click)

    def launch_button_click(self):
        self.processor = HotKeyProcessor(self,
                                         self.keys.active_keys(),
                                         self.get_struct())
        self.processor.setWindowFlags(self.processor.windowFlags() | Qt.WindowModal)
        self.processor.show()
        self.ui.launch_button.setEnabled(False)
        self.processor.closed.connect(self.unblock_launch)
        self.processor.start()

    def browse_button_click(self):
        path = QFileDialog.getExistingDirectory()
        if path:
            self.ui.path_input.setText(path)

    @Slot()
    def unblock_launch(self):
        self.ui.launch_button.setEnabled(True)

    def hotkey_button_click(self):
        self.hotkey_win = HotKeyWindow(self, self.keys)
        self.hotkey_win.setWindowFlags(self.hotkey_win.windowFlags() | Qt.WindowModal)
        self.hotkey_win.show()

    def closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None:
        self.keys.write("keys.json")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LaunchWindow()
    window.show()

    sys.exit(app.exec_())
