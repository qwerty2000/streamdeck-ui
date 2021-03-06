# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'streamdeck_ui/main.ui',
# licensing of 'streamdeck_ui/main.ui' applies.
#
# Created: Sun Oct  6 02:46:55 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.device_list = QtWidgets.QComboBox(self.centralwidget)
        self.device_list.setMinimumSize(QtCore.QSize(400, 0))
        self.device_list.setObjectName("device_list")
        self.horizontalLayout_3.addWidget(self.device_list)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.brightness = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightness.sizePolicy().hasHeightForWidth())
        self.brightness.setSizePolicy(sizePolicy)
        self.brightness.setMinimumSize(QtCore.QSize(200, 0))
        self.brightness.setOrientation(QtCore.Qt.Horizontal)
        self.brightness.setObjectName("brightness")
        self.horizontalLayout_3.addWidget(self.brightness)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pages = QtWidgets.QTabWidget(self.centralwidget)
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet("b")
        self.pages.setObjectName("pages")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pages.addTab(self.page_1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pages.addTab(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pages.addTab(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pages.addTab(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pages.addTab(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pages.addTab(self.page_6, "")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pages.addTab(self.page_7, "")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pages.addTab(self.page_8, "")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pages.addTab(self.page_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pages.addTab(self.tab_10, "")
        self.horizontalLayout.addWidget(self.pages)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.imageButton = QtWidgets.QPushButton(self.groupBox)
        self.imageButton.setObjectName("imageButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.imageButton)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.text = QtWidgets.QLineEdit(self.groupBox)
        self.text.setObjectName("text")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.text)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.command = QtWidgets.QLineEdit(self.groupBox)
        self.command.setObjectName("command")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.command)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.keys = QtWidgets.QLineEdit(self.groupBox)
        self.keys.setObjectName("keys")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.keys)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.write = QtWidgets.QPlainTextEdit(self.groupBox)
        self.write.setObjectName("write")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.write)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.switch_page = QtWidgets.QSpinBox(self.groupBox)
        self.switch_page.setMinimum(0)
        self.switch_page.setMaximum(10)
        self.switch_page.setProperty("value", 0)
        self.switch_page.setObjectName("switch_page")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.switch_page)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.change_brightness = QtWidgets.QSpinBox(self.groupBox)
        self.change_brightness.setMinimum(-99)
        self.change_brightness.setObjectName("change_brightness")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.change_brightness)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1)
        )
        self.label_4.setText(
            QtWidgets.QApplication.translate("MainWindow", "Brightness:", None, -1)
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_1),
            QtWidgets.QApplication.translate("MainWindow", "Page 1", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_2),
            QtWidgets.QApplication.translate("MainWindow", "2", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_3),
            QtWidgets.QApplication.translate("MainWindow", "3", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_4),
            QtWidgets.QApplication.translate("MainWindow", "4", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_5),
            QtWidgets.QApplication.translate("MainWindow", "5", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_6),
            QtWidgets.QApplication.translate("MainWindow", "6", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_7),
            QtWidgets.QApplication.translate("MainWindow", "7", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_8),
            QtWidgets.QApplication.translate("MainWindow", "8", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.page_9),
            QtWidgets.QApplication.translate("MainWindow", "9", None, -1),
        )
        self.pages.setTabText(
            self.pages.indexOf(self.tab_10),
            QtWidgets.QApplication.translate("MainWindow", "10", None, -1),
        )
        self.groupBox.setTitle(
            QtWidgets.QApplication.translate("MainWindow", "Configure Button", None, -1)
        )
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Image:", None, -1))
        self.imageButton.setText(QtWidgets.QApplication.translate("MainWindow", "Choose", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Text:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Command:", None, -1))
        self.label_5.setText(
            QtWidgets.QApplication.translate("MainWindow", "Press Keys:", None, -1)
        )
        self.label_6.setText(
            QtWidgets.QApplication.translate("MainWindow", "Write Text:", None, -1)
        )
        self.label_8.setText(
            QtWidgets.QApplication.translate("MainWindow", "Switch Page:", None, -1)
        )
        self.label_7.setText(
            QtWidgets.QApplication.translate("MainWindow", "Brightness +/-:", None, -1)
        )
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionImport.setText(
            QtWidgets.QApplication.translate("MainWindow", "Import", None, -1)
        )
        self.actionExport.setText(
            QtWidgets.QApplication.translate("MainWindow", "Export", None, -1)
        )
