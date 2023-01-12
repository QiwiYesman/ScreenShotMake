import functools
from functools import partial
from typing import List, Callable, Any, Dict

import PySide2
from PySide2.QtCore import Signal, Slot, Qt
from PySide2.QtWidgets import QWidget, QApplication, QFormLayout, QLabel

from command_reader import HotKey
from defining_area import DefineAreaWindow
from folder import Folder
from keyboard_listener import KeyboardListener
from screen_area import Area
from screenshots import Screenshot
from default_struct import DefaultStruct


class HotKeyProcessor(QWidget):
    closed = Signal()

    process = Signal(type(print))

    def __init__(self, parent, hotkeys: List[HotKey],
                 struct: DefaultStruct):
        super().__init__(parent)
        self.listener = KeyboardListener()
        self.hotkeys: List[HotKey] = hotkeys
        self.area: Area = Area()
        self.folder, \
            self.image_name, \
            self.image_ext, \
            self.paused, \
            self.after_defining_screen, \
            self.screenshot_backend = struct.values
        self.defining = False
        self.process.connect(self.process_func)

        self.deploy_states()
        self.fullscreen()

    def path(self):
        return Folder(self.folder).get_unique_fullpath(f"{self.image_name}.{self.image_ext}")

    def with_state_updating(func: Callable):
        @functools.wraps(func)
        def wrapper(self, *args):
            func(self, *args)
            self.update_states()

        return wrapper

    def deploy_states(self):
        main_layout = QFormLayout()
        self.setLayout(main_layout)
        main_layout.addRow(QLabel("Current area: "),
                           QLabel(f"{self.area.coords}"))

        main_layout.addRow(QLabel("On pause: "),
                           QLabel(f"{self.paused}"))

        main_layout.addRow(QLabel("Screenshot after defining: "),
                           QLabel(f"{self.after_defining_screen}"))

    def update_states(self):
        coord_label: QLabel = self.layout().itemAt(1).widget()
        coord_label.setText(f"{self.area.coords}")

        pause_label: QLabel = self.layout().itemAt(3).widget()
        pause_label.setText(f"{self.paused}")

        screen_define_label: QLabel = self.layout().itemAt(5).widget()
        screen_define_label.setText(f"{self.after_defining_screen}")
        self.adjustSize()

    @Slot(type(print))
    def process_func(self, func):
        func()

    @property
    def funcs(self):
        return (self.fullscreen,
                self.change_area,
                self.screenshot,
                self.pause,
                self.change_screen_after_define,
                self.exit)

    @property
    def hotkeys(self):
        return self._hotkeys

    @hotkeys.setter
    def hotkeys(self, hotkeys: List[HotKey]):
        self._hotkeys = {}
        for i in range(len(hotkeys)):
            self._hotkeys[hotkeys[i].key] = partial(self.process.emit, self.funcs[i])

    def start(self):
        self.listener.stop()
        self.listener = KeyboardListener()
        self.listener.hotkeys = self.hotkeys
        self.listener.start()

    def screenshot(self):
        if not self.paused:
            Screenshot.screenshot_save(self.area.coords, self.screenshot_backend, self.path())

    @with_state_updating
    def change_screen_after_define(self):
        self.after_defining_screen = not self.after_defining_screen

    @with_state_updating
    def pause(self):
        self.paused = not self.paused

    def change_area(self):
        if not self.paused:
            self.paused = True
            defining_window = DefineAreaWindow(self)
            defining_window.setWindowFlags(defining_window.windowFlags() | Qt.WindowModal)
            defining_window.show()
            defining_window.closed.connect(self.set_area)

    @with_state_updating
    def fullscreen(self):
        if not self.paused:
            screen_widget = QApplication.desktop()
            self.area = Area(screen_widget.geometry().getCoords())

    def closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None:
        self.listener.stop()
        self.closed.emit()

    def exit(self):
        self.close()

    @with_state_updating
    @Slot(Area)
    def set_area(self, area: Area):
        self.area = area
        if self.area.x2 < self.area.x1:
            self.area.swap_x()
        if self.area.y2 < self.area.y1:
            self.area.swap_y()
        self.paused = False
        if self.after_defining_screen:
            self.screenshot()
