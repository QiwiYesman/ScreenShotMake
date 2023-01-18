import functools
from functools import partial
from typing import List, Callable

import PySide2
import pyautogui
from PySide2 import QtGui
from PySide2.QtCore import Signal, Slot, Qt
from PySide2.QtGui import QPixmap, QImage
from PySide2.QtWidgets import QWidget, QApplication, QFormLayout, QLabel

from command_reader import HotKey
from defining_area import DefineAreaWindow
from folder import Folder
from keyboard_listener import KeyboardListener
from screen_area import Area
from screenshots import Screenshot
from default_struct import DefaultStruct

pyautogui.PAUSE = float(0)


class HotKeyProcessor(QWidget):
    closed = Signal()

    process = Signal(type(print))

    def __init__(self, parent, hotkeys: List[HotKey],
                 struct: DefaultStruct):
        super().__init__(parent)
        self.listener = KeyboardListener()
        self.hotkeys: List[HotKey] = hotkeys
        self.area: Area = Area()
        self.folder, self.image_name, self.image_ext, \
            self.paused, self.after_defining_screen, self.screenshot_backend, \
            self.define_method = struct.values
        self.defining = False
        self.process.connect(self.process_func)
        self.defining_window = None
        self.deploy_states()
        self.fullscreen()
        self.clipboard = QApplication.clipboard()
        self.clipboard_pause = True
        self.clipboard.dataChanged.connect(self.printscreen_screenshot)

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

    def printscreen_screenshot(self):
        if not self.clipboard_pause:
            fullscreen_image = self.clipboard.image()
            cropped = fullscreen_image.copy(*self.area.geometry)
            pixmap = QPixmap.fromImage(cropped)
            pixmap.save(self.path())
            self.clipboard_pause = True
            QApplication.clipboard().setPixmap(pixmap)

    def backend_screenshot(self):
        im = Screenshot.screenshot(self.area.coords, self.screenshot_backend)
        Screenshot.save(im, self.path())
        im = im.convert("RGBA")
        data = im.tobytes("raw", "RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888)
        QApplication.clipboard().setPixmap(QPixmap.fromImage(qim))

    def screenshot(self):
        if not self.paused:
            if self.screenshot_backend == "printscreen":
                self.clipboard_pause = False
                pyautogui.keyUp("alt")
                pyautogui.keyDown("printscreen")
                pyautogui.keyUp("printscreen")
            else:
                self.backend_screenshot()

    @with_state_updating
    def change_screen_after_define(self):
        self.after_defining_screen = not self.after_defining_screen

    @with_state_updating
    def pause(self):
        self.paused = not self.paused

    def change_area(self):
        if not self.paused:
            self.paused = True

            self.defining_window = DefineAreaWindow(None, self.define_method)
            self.defining_window.setWindowFlags(self.defining_window.windowFlags() | Qt.WindowStaysOnTopHint)
            self.defining_window.activateWindow()
            self.defining_window.show()
            self.defining_window.closed.connect(self.set_area)

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
