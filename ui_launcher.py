# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(593, 236)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 563, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.launch_button = QPushButton(self.verticalLayoutWidget)
        self.launch_button.setObjectName(u"launch_button")

        self.horizontalLayout_4.addWidget(self.launch_button)

        self.hotkey_button = QPushButton(self.verticalLayoutWidget)
        self.hotkey_button.setObjectName(u"hotkey_button")

        self.horizontalLayout_4.addWidget(self.hotkey_button)

        self.settings_button = QPushButton(self.verticalLayoutWidget)
        self.settings_button.setObjectName(u"settings_button")

        self.horizontalLayout_4.addWidget(self.settings_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.browse_button = QPushButton(self.verticalLayoutWidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setMaximumSize(QSize(85, 16777215))

        self.gridLayout.addWidget(self.browse_button, 0, 3, 1, 1)

        self.path_input = QLineEdit(self.verticalLayoutWidget)
        self.path_input.setObjectName(u"path_input")
        self.path_input.setMaximumSize(QSize(283, 16777215))

        self.gridLayout.addWidget(self.path_input, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(83, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(24, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.filename_input = QLineEdit(self.verticalLayoutWidget)
        self.filename_input.setObjectName(u"filename_input")
        self.filename_input.setMaximumSize(QSize(283, 16777215))

        self.horizontalLayout_2.addWidget(self.filename_input)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.extension_input = QLineEdit(self.verticalLayoutWidget)
        self.extension_input.setObjectName(u"extension_input")
        self.extension_input.setMaximumSize(QSize(283, 16777215))

        self.horizontalLayout.addWidget(self.extension_input)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.backend_input = QComboBox(self.verticalLayoutWidget)
        self.backend_input.addItem("")
        self.backend_input.addItem("")
        self.backend_input.addItem("")
        self.backend_input.addItem("")
        self.backend_input.setObjectName(u"backend_input")

        self.horizontalLayout_3.addWidget(self.backend_input)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.launch_button.setText(QCoreApplication.translate("Form", u"Launch", None))
        self.hotkey_button.setText(QCoreApplication.translate("Form", u"Hotkeys", None))
        self.settings_button.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.browse_button.setText(QCoreApplication.translate("Form", u"Browse...", None))
        self.label.setText(QCoreApplication.translate("Form", u"Folder to save", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Default file name", None))
        self.filename_input.setText(QCoreApplication.translate("Form", u"img", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Extension", None))
        self.extension_input.setText(QCoreApplication.translate("Form", u"png", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Backend", None))
        self.backend_input.setItemText(0, QCoreApplication.translate("Form", u"mss", None))
        self.backend_input.setItemText(1, QCoreApplication.translate("Form", u"pil", None))
        self.backend_input.setItemText(2, QCoreApplication.translate("Form", u"scrot", None))
        self.backend_input.setItemText(3, QCoreApplication.translate("Form", u"gnome-screenshot", None))

    # retranslateUi

