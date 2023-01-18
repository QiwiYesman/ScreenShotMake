from typing import List

import PySide2
from PySide2.QtGui import QColor, QPainter, QBrush, QCursor
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import Qt, Signal, QEvent
from screen_area import Area


class TransparentWindow(QWidget):
    def __init__(self, parent=None, color=Qt.white):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, False)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.set_color(color)

    def set_color(self, color: QColor, transparent: int = 70):
        p = self.palette()
        colors = QColor(color).getRgb()
        p.setColor(self.backgroundRole(), QColor(colors[0], colors[1], colors[2], transparent))
        self.setPalette(p)


class DefineAreaWindow(TransparentWindow):
    closed = Signal(Area)

    def __init__(self, parent=None, method="Key"):
        super().__init__(parent)
        self.define_events = {}
        self.define_method = method
        self.update_method()
        desktop = QApplication.desktop().geometry()

        self.setGeometry(desktop)
        self.set_color(Qt.white, 0)
        self.is_defining = False
        self.to_finish = True
        self.area = Area()

    def update_method(self):
        if self.define_method == "Mouse":
            self.define_events["press"] = QEvent.MouseButtonPress, self.on_mouse_press
            self.define_events["release"] = QEvent.MouseButtonRelease, self.on_mouse_release
        elif self.define_method == "Key":
            self.define_events["press"] = QEvent.KeyPress, self.on_key_press
            self.define_events["release"] = QEvent.KeyRelease, self.on_key_release

    def get_rect_area(self) -> List:
        geometry = list(self.area.geometry)
        if geometry[2] < 0:
            geometry[0] += geometry[2]
            geometry[2] *= -1
        if geometry[3] < 0:
            geometry[1] += geometry[3]
            geometry[3] *= -1
        return geometry

    def paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 255, 150))
        if self.is_defining or self.to_finish:
            geometry = self.get_rect_area()
            painter.setCompositionMode(QPainter.CompositionMode_Source)
            painter.setBrush(QBrush(QColor(255, 255, 255, 0), Qt.SolidPattern))
            painter.drawRect(*geometry)

    def created(self):
        if "define_events" in self.__dict__:
            self.created = lambda: True
            return True
        return False

    def event(self, event: PySide2.QtCore.QEvent) -> bool:
        if self.created():
            if event.type() == self.define_events["press"][0]:
                self.define_events["press"][1](event)
            elif event.type() == self.define_events["release"][0]:
                self.define_events["release"][1](event)
        return QWidget.event(self, event)

    def on_mouse_press(self, event: PySide2.QtGui.QMouseEvent):
        cursor = QCursor()
        x, y = cursor.pos().x(), cursor.pos().y()

        button = event.button()
        if button == Qt.LeftButton and not self.is_defining:
            self.area.coords = x, y, x, y
            self.is_defining = True
            self.setMouseTracking(True)
            self.to_finish = False
        elif button == Qt.LeftButton and self.is_defining:
            self.to_finish = True
        elif button == Qt.RightButton:
            self.update()
            self.close()

    def on_mouse_release(self, event: PySide2.QtGui.QMouseEvent):
        button = event.button()
        if button == Qt.LeftButton and self.is_defining:
            if self.to_finish:
                self.setMouseTracking(False)
                self.is_defining = False

    def on_key_press(self, event: PySide2.QtGui.QKeyEvent):
        cursor = QCursor()
        x, y = cursor.pos().x(), cursor.pos().y()

        button = event.key()
        if button == Qt.Key_Space and not self.is_defining:
            self.area.coords = x, y, x, y
            self.is_defining = True
            self.setMouseTracking(True)
            self.to_finish = False
        elif button == Qt.Key_Space and self.is_defining:
            self.to_finish = True
        elif button == Qt.Key_Escape:
            self.update()
            self.close()

    def on_key_release(self, event: PySide2.QtGui.QKeyEvent):
        button = event.key()
        if button == Qt.Key_Space and self.is_defining:
            if self.to_finish:
                self.setMouseTracking(False)
                self.is_defining = False

    def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
        self.area.x2, self.area.y2 = event.pos().x(), event.pos().y()
        self.update()

    def closeEvent(self, event) -> None:
        self.hide()
        self.closed.emit(self.area)
