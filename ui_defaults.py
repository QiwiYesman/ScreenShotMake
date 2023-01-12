# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'defaults.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class SettingsWindowUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(472, 318)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 451, 241))
        self.main_grid_layout = QGridLayout(self.gridLayoutWidget)
        self.main_grid_layout.setObjectName(u"main_grid_layout")
        self.main_grid_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.main_grid_layout.setHorizontalSpacing(15)
        self.main_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.pause_switch = QPushButton(self.gridLayoutWidget)
        self.pause_switch.setObjectName(u"pause_switch")
        self.pause_switch.setMaximumSize(QSize(85, 16777215))

        self.main_grid_layout.addWidget(self.pause_switch, 3, 2, 1, 1)

        self.browse_button = QPushButton(self.gridLayoutWidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setMaximumSize(QSize(85, 16777215))

        self.main_grid_layout.addWidget(self.browse_button, 0, 2, 1, 1)

        self.screen_define_switch = QPushButton(self.gridLayoutWidget)
        self.screen_define_switch.setObjectName(u"screen_define_switch")
        self.screen_define_switch.setMaximumSize(QSize(85, 16777215))

        self.main_grid_layout.addWidget(self.screen_define_switch, 4, 2, 1, 1)

        self.image_extension_input = QLineEdit(self.gridLayoutWidget)
        self.image_extension_input.setObjectName(u"image_extension_input")
        self.image_extension_input.setMaximumSize(QSize(283, 16777215))

        self.main_grid_layout.addWidget(self.image_extension_input, 2, 1, 1, 1)

        self.image_name_input = QLineEdit(self.gridLayoutWidget)
        self.image_name_input.setObjectName(u"image_name_input")
        self.image_name_input.setMaximumSize(QSize(283, 16777215))

        self.main_grid_layout.addWidget(self.image_name_input, 1, 1, 1, 1)

        self.path_input = QLineEdit(self.gridLayoutWidget)
        self.path_input.setObjectName(u"path_input")
        self.path_input.setMaximumSize(QSize(283, 16777215))

        self.main_grid_layout.addWidget(self.path_input, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QSize(83, 16777215))

        self.main_grid_layout.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.main_grid_layout.addWidget(self.label_16, 4, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMaximumSize(QSize(83, 16777215))

        self.main_grid_layout.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.main_grid_layout.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QSize(83, 16777215))

        self.main_grid_layout.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.main_grid_layout.addWidget(self.label_17, 5, 0, 1, 1)

        self.paused_label = QLabel(self.gridLayoutWidget)
        self.paused_label.setObjectName(u"paused_label")

        self.main_grid_layout.addWidget(self.paused_label, 3, 1, 1, 1)

        self.screen_definin_label = QLabel(self.gridLayoutWidget)
        self.screen_definin_label.setObjectName(u"screen_definin_label")

        self.main_grid_layout.addWidget(self.screen_definin_label, 4, 1, 1, 1)

        self.backend_choice = QComboBox(self.gridLayoutWidget)
        self.backend_choice.addItem("")
        self.backend_choice.addItem("")
        self.backend_choice.addItem("")
        self.backend_choice.addItem("")
        self.backend_choice.setObjectName(u"backend_choice")

        self.main_grid_layout.addWidget(self.backend_choice, 5, 1, 1, 1)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 260, 451, 51))
        self.last_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.last_layout.setObjectName(u"last_layout")
        self.last_layout.setContentsMargins(0, 0, 0, 0)
        self.confirm_button = QPushButton(self.horizontalLayoutWidget)
        self.confirm_button.setObjectName(u"confirm_button")

        self.last_layout.addWidget(self.confirm_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.last_layout.addItem(self.horizontalSpacer_5)

        self.cancel_button = QPushButton(self.horizontalLayoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.last_layout.addWidget(self.cancel_button)

        self.last_layout.setStretch(0, 3)
        self.last_layout.setStretch(1, 6)
        self.last_layout.setStretch(2, 3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pause_switch.setText(QCoreApplication.translate("Form", u"Switch", None))
        self.browse_button.setText(QCoreApplication.translate("Form", u"Browse...", None))
        self.screen_define_switch.setText(QCoreApplication.translate("Form", u"Switch", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Folder to save", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Screen after defining", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Image name", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Image extension", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Paused", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Screenshot backend", None))
        self.paused_label.setText(QCoreApplication.translate("Form", u"False", None))
        self.screen_definin_label.setText(QCoreApplication.translate("Form", u"True", None))
        self.backend_choice.setItemText(0, QCoreApplication.translate("Form", u"mss", None))
        self.backend_choice.setItemText(1, QCoreApplication.translate("Form", u"pil", None))
        self.backend_choice.setItemText(2, QCoreApplication.translate("Form", u"scrot", None))
        self.backend_choice.setItemText(3, QCoreApplication.translate("Form", u"gnome-screenshot", None))

        self.confirm_button.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

