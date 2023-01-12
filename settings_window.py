import copy

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget, QFileDialog

from default_struct import DefaultStruct
from ui_defaults import SettingsWindowUi


class SettingsWindow(QWidget):
    closed = Signal(DefaultStruct)

    def __init__(self, defaults: DefaultStruct, parent=None):
        super().__init__(parent)
        self.ui = SettingsWindowUi()
        self.ui.setupUi(self)
        self.deploy_defaults(defaults)
        self.set_connections()

    def deploy_defaults(self, defaults: DefaultStruct):
        self.ui.path_input.setText(defaults.default_path)
        self.ui.image_name_input.setText(defaults.default_image_name)
        self.ui.image_extension_input.setText(defaults.default_image_ext)
        self.ui.paused_label.setText(f"{defaults.default_is_paused}")
        self.ui.screen_definin_label.setText(f"{defaults.default_after_screen_defining}")
        self.ui.backend_choice.setCurrentText(defaults.default_backend)

    def get_struct(self):
        return DefaultStruct(
            default_path=self.ui.path_input.text(),
            default_backend=self.ui.backend_choice.currentText(),
            default_image_name=self.ui.image_name_input.text(),
            default_image_ext=self.ui.image_extension_input.text(),
            default_is_paused=self.ui.paused_label.text() == 'True',
            default_after_screen_defining=self.ui.screen_definin_label.text() == 'True'
        )

    def browse_button_click(self):
        path = QFileDialog.getExistingDirectory(parent=self)
        if path:
            self.ui.path_input.setText(path)

    def accept(self, to_accept: bool):
        if to_accept:
            self.closed.emit(self.get_struct())
        self.close()

    def switch_pause(self):
        text = self.ui.paused_label.text()
        self.ui.paused_label.setText(
            f"{not text == 'True'}")

    def switch_screen_define(self):
        text = self.ui.screen_definin_label.text()
        self.ui.screen_definin_label.setText(
            f"{not text == 'True'}")

    def set_connections(self):
        self.ui.pause_switch.clicked.connect(self.switch_pause)
        self.ui.screen_define_switch.clicked.connect(self.switch_screen_define)
        self.ui.browse_button.clicked.connect(self.browse_button_click)
        self.ui.confirm_button.clicked.connect(lambda x: self.accept(True))
        self.ui.cancel_button.clicked.connect(lambda x: self.accept(False))
