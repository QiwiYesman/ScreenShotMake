from typing import List

import PySide2
from PySide2 import QtCore
from PySide2.QtCore import QDir, Slot, Qt
from PySide2.QtWidgets import QFileDialog

from generated_ui import Ui_Form
from defining_area import DefineAreaWindow, Area, QWidget, QApplication
from command_reader import HotKey, KeyMapper
from hotkeys_window import HotKeyWindow
import sys

from folder import Folder
from hotkey_processor import HotKeyProcessor


class LaunchWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.set_connections()
        self.default_path()
        self.keys = KeyMapper.from_file("keys.json")
        self.screenshot_area = Area()
        self.win: DefineAreaWindow = None
        self.hotkey_win: HotKeyWindow = None
        self.processor: HotKeyProcessor = None

    def set_connections(self):
        self.ui.launch_button.clicked.connect(self.launch_button_click)
        self.ui.hotkey_button.clicked.connect(self.hotkey_button_click)
        self.ui.browse_button.clicked.connect(self.browse_button_click)

    @property
    def folder(self):
        return Folder(self.ui.path_input.text())

    @property
    def file_name(self):
        return self.ui.filename_input.text() + "." + self.ui.extension_input.text()

    def launch_button_click(self):
        self.processor = HotKeyProcessor(None,
                                         self.keys.active_keys(),
                                         self.folder,
                                         self.file_name)
        self.ui.launch_button.setEnabled(False)
        self.processor.closed.connect(self.unblock_launch)
        self.processor.start()

    def browse_button_click(self):
        path = QFileDialog.getExistingDirectory()
        if path:
            self.ui.path_input.setText(path)

    def default_path(self):
        folder = Folder(QDir.currentPath()).create("img")
        self.ui.path_input.setText(str(folder.folder))

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
