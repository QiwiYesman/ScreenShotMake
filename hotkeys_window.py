from functools import partial
from typing import List

import PySide2
from PySide2 import QtCore
from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QGridLayout, QVBoxLayout, QComboBox

from assign_key_window import AssignHotKey
from command_reader import HotKey, KeyMapper
import copy


class HotKeyWindow(QWidget):
    closed = Signal()

    def __init__(self, parent=None, keys: KeyMapper = None):
        super().__init__(parent)
        self.keys = copy.deepcopy(keys)
        self.key_layouts: List[QHBoxLayout] = []
        self.vertical_layout = QVBoxLayout(self)
        self.grid = QGridLayout()
        self.map_choice = QComboBox()
        self.load_ui()
        self.deploy_hotkeys(self.keys.active_map_name)
        self.assigning_keys = []
        self.rename_button: QPushButton = None

    @property
    def current_map(self) -> str:
        return self.map_choice.currentText()

    def deploy_map_names(self):
        self.map_choice.blockSignals(True)
        for i in reversed(range(self.map_choice.count())):
            self.map_choice.removeItem(i)
        self.map_choice.blockSignals(False)
        for key in self.keys.maps:
            self.map_choice.addItem(key)

    def deploy_current_map(self):
        if self.map_choice.isEditable():
            self.map_choice.setEditable(False)
        current_name = self.current_map
        self.deploy_hotkeys(current_name)
        self.reload_map_layout()

    def exit(self, confirm_changes: bool = False):
        if confirm_changes:
            self.parent().keys = self.keys
        self.close()

    def edit_current_name(self, value: bool):
        if not value:
            new_name = self.current_map
            self.map_choice.setEditable(False)
            if not self.is_existing_map_name(new_name):
                current_name = self.current_map
                self.keys.map(new_name, self.keys.maps.pop(current_name))
                self.deploy_map_names()
        else:
            self.map_choice.setEditable(True)

    def add_non_default_buttons_to_map_layout(self, layout: QHBoxLayout):
        rename_button = QPushButton("Rename")
        rename_button.setCheckable(True)
        rename_button.clicked.connect(
            lambda x: self.edit_current_name(rename_button.isChecked()))
        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.remove_current_map)

        for w in rename_button, remove_button:
            layout.addWidget(w)

    def reload_map_layout(self):
        map_layout: QHBoxLayout = self.vertical_layout.itemAt(0)
        activate_button: QPushButton = map_layout.itemAt(1).widget()
        if self.current_map == self.keys.active_map_name:
            activate_button.setChecked(True)
            activate_button.setEnabled(False)
        else:
            activate_button.setChecked(False)
            activate_button.setEnabled(True)
        if self.current_map == "default":
            if map_layout.count() > 3:
                for i in range(2):
                    item = map_layout.itemAt(3).widget()
                    map_layout.removeWidget(item)
                    item.setParent(None)
        else:
            if map_layout.count() <= 3:
                self.add_non_default_buttons_to_map_layout(map_layout)

    def activate_current_map(self):
        sender: QPushButton = self.sender()
        if sender.isChecked():
            sender.setDisabled(True)
            self.keys.active_map_name = self.current_map

    def remove_map_by_name(self, name: str):
        for i in range(self.map_choice.count()):
            if self.map_choice.itemText(i) == name:
                self.map_choice.removeItem(i)
                break

    def remove_current_map(self):
        if self.keys.active_map_name == self.current_map:
            self.keys.active_map_name = "default"
        self.keys.maps.pop(self.current_map)
        self.remove_map_by_name(self.current_map)
        self.deploy_current_map()

    def is_existing_map_name(self, map_name: str):
        return map_name in self.keys.maps

    def copy_name(self, map_name: str):
        new_name = map_name + "_copy"
        i = 1
        if self.is_existing_map_name(new_name):
            while self.is_existing_map_name(f"{new_name}_{i}"):
                i += 1
            return f"{new_name}_{i}"
        else:
            return new_name

    def copy_current_map(self):
        new_name = self.copy_name(self.current_map)
        self.keys.maps[new_name] = copy.deepcopy(self.keys.maps[self.current_map])
        self.map_choice.addItem(new_name)

    def load_ui(self):
        self.setLayout(self.vertical_layout)
        self.map_choice.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        self.deploy_map_names()
        self.map_choice.currentIndexChanged.connect(self.deploy_current_map)

        map_layout = QHBoxLayout()

        last_layout = QHBoxLayout()
        confirm_button = QPushButton("Confirm")
        confirm_button.clicked.connect(lambda: self.exit(True))
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(lambda: self.exit(False))

        activate_button = QPushButton("Set active")
        activate_button.clicked.connect(self.activate_current_map)
        activate_button.setCheckable(True)
        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.copy_current_map)

        for w in self.map_choice, activate_button, copy_button:
            map_layout.addWidget(w)
        for w in confirm_button, cancel_button:
            last_layout.addWidget(w)

        self.vertical_layout.addLayout(map_layout)
        self.vertical_layout.addLayout(self.grid)
        self.vertical_layout.addLayout(last_layout)
        self.reload_map_layout()
        self.show()

    def clear(self):
        for i in range(self.grid.rowCount()):
            for j in reversed(range(self.grid.columnCount())):
                if self.grid.itemAtPosition(i, j):
                    widget = self.grid.itemAtPosition(i, j).widget()
                    self.grid.removeWidget(widget)
                    widget.setParent(None)

    def create_assigning_window(self, index: int):
        window = AssignHotKey(self, index)
        window.closed.connect(self.change_hotkey)
        self.assigning_keys.append(window)

    def deploy_key_layout(self, index: int, key: HotKey):
        self.grid.addWidget(QLabel(key.key), index, 1)
        self.grid.addWidget(QLabel(key.command_name), index, 0)
        if self.map_choice.currentText() != "default":
            button = QPushButton("Change")
            button.clicked.connect(partial(self.create_assigning_window, index))
            self.grid.addWidget(button, index, 2)

    def deploy_hotkeys(self, map_name: str):
        self.clear()
        hotkeys = self.keys.keys(map_name)
        i = 0
        for key in hotkeys:
            self.deploy_key_layout(i, key)
            i += 1

    @Slot(QWidget, int, list)
    def change_hotkey(self, changer: QWidget, index: int, keys: List[str]):
        if not keys:
            return
        self.keys.keys(self.current_map)[index].key = keys
        self.assigning_keys.remove(changer)
        self.deploy_current_map()

    def closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None:
        self.closed.emit()
