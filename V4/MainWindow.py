# Form implementation generated from reading ui file 'v4.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 900, 575))
        self.tabWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.connectA = QtWidgets.QPushButton(parent=self.tab)
        self.connectA.setGeometry(QtCore.QRect(190, 10, 75, 31))
        self.connectA.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.connectA.setObjectName("connectA")
        self.connectLabel_a = QtWidgets.QLabel(parent=self.tab)
        self.connectLabel_a.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.connectLabel_a.setFont(font)
        self.connectLabel_a.setObjectName("connectLabel_a")
        self.connectB = QtWidgets.QPushButton(parent=self.tab)
        self.connectB.setGeometry(QtCore.QRect(450, 10, 75, 31))
        self.connectB.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.connectB.setObjectName("connectB")
        self.connectLabel_b = QtWidgets.QLabel(parent=self.tab)
        self.connectLabel_b.setGeometry(QtCore.QRect(270, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.connectLabel_b.setFont(font)
        self.connectLabel_b.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.connectLabel_b.setObjectName("connectLabel_b")
        self.groupBox_Ax = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_Ax.setGeometry(QtCore.QRect(10, 50, 261, 111))
        self.groupBox_Ax.setAutoFillBackground(False)
        self.groupBox_Ax.setTitle("")
        self.groupBox_Ax.setObjectName("groupBox_Ax")
        self.xDisplay_a = QtWidgets.QLabel(parent=self.groupBox_Ax)
        self.xDisplay_a.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.xDisplay_a.setFont(font)
        self.xDisplay_a.setObjectName("xDisplay_a")
        self.xGround_a = QtWidgets.QPushButton(parent=self.groupBox_Ax)
        self.xGround_a.setGeometry(QtCore.QRect(130, 60, 81, 32))
        self.xGround_a.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.xGround_a.setObjectName("xGround_a")
        self.xChange_a = QtWidgets.QDoubleSpinBox(parent=self.groupBox_Ax)
        self.xChange_a.setGeometry(QtCore.QRect(130, 10, 81, 31))
        self.xChange_a.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.xChange_a.setObjectName("xChange_a")
        self.xGround_a.raise_()
        self.xChange_a.raise_()
        self.xDisplay_a.raise_()
        self.groupBox_Ay = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_Ay.setGeometry(QtCore.QRect(10, 160, 261, 111))
        self.groupBox_Ay.setAutoFillBackground(False)
        self.groupBox_Ay.setTitle("")
        self.groupBox_Ay.setObjectName("groupBox_Ay")
        self.yDisplay_a = QtWidgets.QLabel(parent=self.groupBox_Ay)
        self.yDisplay_a.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.yDisplay_a.setFont(font)
        self.yDisplay_a.setObjectName("yDisplay_a")
        self.yGround_a = QtWidgets.QPushButton(parent=self.groupBox_Ay)
        self.yGround_a.setGeometry(QtCore.QRect(130, 60, 81, 32))
        self.yGround_a.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.yGround_a.setObjectName("yGround_a")
        self.yChange_a = QtWidgets.QDoubleSpinBox(parent=self.groupBox_Ay)
        self.yChange_a.setGeometry(QtCore.QRect(130, 10, 81, 31))
        self.yChange_a.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.yChange_a.setObjectName("yChange_a")
        self.yGround_a.raise_()
        self.yChange_a.raise_()
        self.yDisplay_a.raise_()
        self.groupBox_Az = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_Az.setGeometry(QtCore.QRect(10, 270, 261, 111))
        self.groupBox_Az.setAutoFillBackground(False)
        self.groupBox_Az.setTitle("")
        self.groupBox_Az.setObjectName("groupBox_Az")
        self.zDisplay_a = QtWidgets.QLabel(parent=self.groupBox_Az)
        self.zDisplay_a.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zDisplay_a.setFont(font)
        self.zDisplay_a.setObjectName("zDisplay_a")
        self.zGround_a = QtWidgets.QPushButton(parent=self.groupBox_Az)
        self.zGround_a.setGeometry(QtCore.QRect(130, 60, 81, 32))
        self.zGround_a.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.zGround_a.setObjectName("zGround_a")
        self.zChange_a = QtWidgets.QDoubleSpinBox(parent=self.groupBox_Az)
        self.zChange_a.setGeometry(QtCore.QRect(130, 10, 81, 31))
        self.zChange_a.setObjectName("zChange_a")
        self.zGround_a.raise_()
        self.zChange_a.raise_()
        self.zDisplay_a.raise_()
        self.groupBox_By = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_By.setGeometry(QtCore.QRect(270, 160, 261, 111))
        self.groupBox_By.setAutoFillBackground(False)
        self.groupBox_By.setTitle("")
        self.groupBox_By.setObjectName("groupBox_By")
        self.yDisplay_b = QtWidgets.QLabel(parent=self.groupBox_By)
        self.yDisplay_b.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.yDisplay_b.setFont(font)
        self.yDisplay_b.setObjectName("yDisplay_b")
        self.yGround_b = QtWidgets.QPushButton(parent=self.groupBox_By)
        self.yGround_b.setGeometry(QtCore.QRect(130, 60, 81, 32))
        self.yGround_b.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.yGround_b.setObjectName("yGround_b")
        self.yChange_b = QtWidgets.QDoubleSpinBox(parent=self.groupBox_By)
        self.yChange_b.setGeometry(QtCore.QRect(130, 10, 81, 31))
        self.yChange_b.setObjectName("yChange_b")
        self.yGround_b.raise_()
        self.yChange_b.raise_()
        self.yDisplay_b.raise_()
        self.groupBox_Bx = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_Bx.setGeometry(QtCore.QRect(270, 50, 261, 111))
        self.groupBox_Bx.setAutoFillBackground(False)
        self.groupBox_Bx.setTitle("")
        self.groupBox_Bx.setObjectName("groupBox_Bx")
        self.xDisplay_b = QtWidgets.QLabel(parent=self.groupBox_Bx)
        self.xDisplay_b.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.xDisplay_b.setFont(font)
        self.xDisplay_b.setObjectName("xDisplay_b")
        self.xGround_b = QtWidgets.QPushButton(parent=self.groupBox_Bx)
        self.xGround_b.setGeometry(QtCore.QRect(130, 60, 81, 32))
        self.xGround_b.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.xGround_b.setObjectName("xGround_b")
        self.xChange_b = QtWidgets.QDoubleSpinBox(parent=self.groupBox_Bx)
        self.xChange_b.setGeometry(QtCore.QRect(130, 10, 81, 31))
        self.xChange_b.setObjectName("xChange_b")
        self.xGround_b.raise_()
        self.xChange_b.raise_()
        self.xDisplay_b.raise_()
        self.groupBox_Bz = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_Bz.setGeometry(QtCore.QRect(270, 270, 261, 111))
        self.groupBox_Bz.setAutoFillBackground(False)
        self.groupBox_Bz.setTitle("")
        self.groupBox_Bz.setObjectName("groupBox_Bz")
        self.zDisplay_b = QtWidgets.QLabel(parent=self.groupBox_Bz)
        self.zDisplay_b.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zDisplay_b.setFont(font)
        self.zDisplay_b.setObjectName("zDisplay_b")
        self.zGround_b = QtWidgets.QPushButton(parent=self.groupBox_Bz)
        self.zGround_b.setGeometry(QtCore.QRect(130, 60, 81, 32))
        self.zGround_b.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.zGround_b.setObjectName("zGround_b")
        self.zChange_b = QtWidgets.QDoubleSpinBox(parent=self.groupBox_Bz)
        self.zChange_b.setGeometry(QtCore.QRect(130, 10, 81, 31))
        self.zChange_b.setObjectName("zChange_b")
        self.zGround_b.raise_()
        self.zChange_b.raise_()
        self.zDisplay_b.raise_()
        self.connectLabel_power = QtWidgets.QLabel(parent=self.tab)
        self.connectLabel_power.setGeometry(QtCore.QRect(550, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.connectLabel_power.setFont(font)
        self.connectLabel_power.setObjectName("connectLabel_power")
        self.connectPower = QtWidgets.QPushButton(parent=self.tab)
        self.connectPower.setGeometry(QtCore.QRect(770, 10, 75, 31))
        self.connectPower.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.connectPower.setObjectName("connectPower")
        self.powerDisplay = QtWidgets.QLabel(parent=self.tab)
        self.powerDisplay.setGeometry(QtCore.QRect(580, 50, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.powerDisplay.setFont(font)
        self.powerDisplay.setObjectName("powerDisplay")
        self.groupBox_Meter = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_Meter.setGeometry(QtCore.QRect(560, 50, 281, 151))
        self.groupBox_Meter.setTitle("")
        self.groupBox_Meter.setObjectName("groupBox_Meter")
        self.wavelengthEdit = QtWidgets.QLineEdit(parent=self.groupBox_Meter)
        self.wavelengthEdit.setGeometry(QtCore.QRect(210, 90, 51, 20))
        self.wavelengthEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.wavelengthEdit.setObjectName("wavelengthEdit")
        self.lambdaLabel = QtWidgets.QLabel(parent=self.groupBox_Meter)
        self.lambdaLabel.setGeometry(QtCore.QRect(200, 90, 21, 21))
        self.lambdaLabel.setObjectName("lambdaLabel")
        self.wavelengthApply = QtWidgets.QPushButton(parent=self.groupBox_Meter)
        self.wavelengthApply.setGeometry(QtCore.QRect(210, 120, 51, 23))
        self.wavelengthApply.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.wavelengthApply.setObjectName("wavelengthApply")
        self.groundAll_b = QtWidgets.QPushButton(parent=self.tab)
        self.groundAll_b.setGeometry(QtCore.QRect(400, 390, 81, 32))
        self.groundAll_b.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.groundAll_b.setObjectName("groundAll_b")
        self.groundAll_a = QtWidgets.QPushButton(parent=self.tab)
        self.groundAll_a.setGeometry(QtCore.QRect(140, 390, 81, 32))
        self.groundAll_a.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.groundAll_a.setObjectName("groundAll_a")
        self.groupBox_autoAlign = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox_autoAlign.setGeometry(QtCore.QRect(560, 210, 281, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_autoAlign.setFont(font)
        self.groupBox_autoAlign.setObjectName("groupBox_autoAlign")
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBox_autoAlign)
        self.spinBox.setGeometry(QtCore.QRect(210, 40, 51, 22))
        self.spinBox.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.spinBox.setObjectName("spinBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox_autoAlign)
        self.lineEdit.setGeometry(QtCore.QRect(210, 70, 51, 20))
        self.lineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox_autoAlign)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 100, 51, 20))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox_autoAlign)
        self.label.setGeometry(QtCore.QRect(140, 40, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_autoAlign)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_autoAlign)
        self.label_3.setGeometry(QtCore.QRect(140, 100, 61, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton.setGeometry(QtCore.QRect(570, 250, 81, 31))
        self.pushButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 300, 81, 31))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.powerDisplay_unit = QtWidgets.QLabel(parent=self.tab)
        self.powerDisplay_unit.setGeometry(QtCore.QRect(700, 50, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.powerDisplay_unit.setFont(font)
        self.powerDisplay_unit.setText("")
        self.powerDisplay_unit.setObjectName("powerDisplay_unit")
        self.groupBox_Meter.raise_()
        self.connectA.raise_()
        self.connectLabel_a.raise_()
        self.connectB.raise_()
        self.connectLabel_b.raise_()
        self.groupBox_Ax.raise_()
        self.groupBox_Ay.raise_()
        self.groupBox_Az.raise_()
        self.groupBox_By.raise_()
        self.groupBox_Bx.raise_()
        self.groupBox_Bz.raise_()
        self.connectLabel_power.raise_()
        self.connectPower.raise_()
        self.powerDisplay.raise_()
        self.groundAll_b.raise_()
        self.groundAll_a.raise_()
        self.groupBox_autoAlign.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.powerDisplay_unit.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.osaTab = QtWidgets.QWidget()
        self.osaTab.setObjectName("osaTab")
        self.plotWidget = PlotWidget(parent=self.osaTab)
        self.plotWidget.setGeometry(QtCore.QRect(140, 20, 741, 501))
        self.plotWidget.setObjectName("plotWidget")
        self.osaRepeatButton = QtWidgets.QPushButton(parent=self.osaTab)
        self.osaRepeatButton.setGeometry(QtCore.QRect(20, 150, 101, 41))
        self.osaRepeatButton.setObjectName("osaRepeatButton")
        self.osaSweepButton = QtWidgets.QPushButton(parent=self.osaTab)
        self.osaSweepButton.setGeometry(QtCore.QRect(20, 90, 101, 41))
        self.osaSweepButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.osaSweepButton.setObjectName("osaSweepButton")
        self.osaConnectButton = QtWidgets.QPushButton(parent=self.osaTab)
        self.osaConnectButton.setGeometry(QtCore.QRect(20, 30, 101, 41))
        self.osaConnectButton.setObjectName("osaConnectButton")
        self.groupBox = QtWidgets.QGroupBox(parent=self.osaTab)
        self.groupBox.setGeometry(QtCore.QRect(20, 390, 101, 131))
        self.groupBox.setObjectName("groupBox")
        self.numWindowsSpin = QtWidgets.QSpinBox(parent=self.groupBox)
        self.numWindowsSpin.setGeometry(QtCore.QRect(60, 30, 31, 22))
        self.numWindowsSpin.setAutoFillBackground(False)
        self.numWindowsSpin.setReadOnly(False)
        self.numWindowsSpin.setObjectName("numWindowsSpin")
        self.numWindowsLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.numWindowsLabel.setGeometry(QtCore.QRect(10, 30, 51, 20))
        self.numWindowsLabel.setObjectName("numWindowsLabel")
        self.windowStartButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.windowStartButton.setGeometry(QtCore.QRect(10, 70, 81, 23))
        self.windowStartButton.setObjectName("windowStartButton")
        self.saveDataCheckbox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.saveDataCheckbox.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.saveDataCheckbox.setObjectName("saveDataCheckbox")
        self.numWindowsSpin.raise_()
        self.windowStartButton.raise_()
        self.saveDataCheckbox.raise_()
        self.numWindowsLabel.raise_()
        self.osaSetLinButton = QtWidgets.QPushButton(parent=self.osaTab)
        self.osaSetLinButton.setGeometry(QtCore.QRect(20, 210, 101, 41))
        self.osaSetLinButton.setObjectName("osaSetLinButton")
        self.osaSetLogButton = QtWidgets.QPushButton(parent=self.osaTab)
        self.osaSetLogButton.setGeometry(QtCore.QRect(20, 270, 101, 41))
        self.osaSetLogButton.setObjectName("osaSetLogButton")
        self.osaSaveButton = QtWidgets.QPushButton(parent=self.osaTab)
        self.osaSaveButton.setGeometry(QtCore.QRect(20, 330, 101, 41))
        self.osaSaveButton.setObjectName("osaSaveButton")
        self.printButton = QtWidgets.QPushButton(parent=self.osaTab)
        self.printButton.setGeometry(QtCore.QRect(800, 520, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.printButton.setFont(font)
        self.printButton.setObjectName("printButton")
        self.tabWidget.addTab(self.osaTab, "")
        self.viewTab = QtWidgets.QWidget()
        self.viewTab.setObjectName("viewTab")
        self.graphWidget = PlotWidget(parent=self.viewTab)
        self.graphWidget.setGeometry(QtCore.QRect(110, 10, 771, 521))
        self.graphWidget.setObjectName("graphWidget")
        self.addPlotButton = QtWidgets.QPushButton(parent=self.viewTab)
        self.addPlotButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.addPlotButton.setObjectName("addPlotButton")
        self.listWidget = QtWidgets.QListWidget(parent=self.viewTab)
        self.listWidget.setGeometry(QtCore.QRect(10, 140, 91, 131))
        self.listWidget.setObjectName("listWidget")
        self.removePlotButton = QtWidgets.QPushButton(parent=self.viewTab)
        self.removePlotButton.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.removePlotButton.setObjectName("removePlotButton")
        self.clearPlotButton = QtWidgets.QPushButton(parent=self.viewTab)
        self.clearPlotButton.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.clearPlotButton.setObjectName("clearPlotButton")
        self.colorButton = QtWidgets.QPushButton(parent=self.viewTab)
        self.colorButton.setGeometry(QtCore.QRect(20, 290, 75, 23))
        self.colorButton.setObjectName("colorButton")
        self.tabWidget.addTab(self.viewTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(parent=self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionpower_meter_setting = QtGui.QAction(parent=MainWindow)
        self.actionpower_meter_setting.setObjectName("actionpower_meter_setting")
        self.actionOSA_settings = QtGui.QAction(parent=MainWindow)
        self.actionOSA_settings.setObjectName("actionOSA_settings")
        self.actionview_COM_ports = QtGui.QAction(parent=MainWindow)
        self.actionview_COM_ports.setObjectName("actionview_COM_ports")
        self.menuOptions.addAction(self.actionview_COM_ports)
        self.menuOptions.addAction(self.actionpower_meter_setting)
        self.menuOptions.addAction(self.actionOSA_settings)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.xChange_a, self.yChange_a)
        MainWindow.setTabOrder(self.yChange_a, self.zChange_a)
        MainWindow.setTabOrder(self.zChange_a, self.xChange_b)
        MainWindow.setTabOrder(self.xChange_b, self.yChange_b)
        MainWindow.setTabOrder(self.yChange_b, self.zChange_b)
        MainWindow.setTabOrder(self.zChange_b, self.numWindowsSpin)
        MainWindow.setTabOrder(self.numWindowsSpin, self.windowStartButton)
        MainWindow.setTabOrder(self.windowStartButton, self.osaSetLinButton)
        MainWindow.setTabOrder(self.osaSetLinButton, self.osaConnectButton)
        MainWindow.setTabOrder(self.osaConnectButton, self.osaSetLogButton)
        MainWindow.setTabOrder(self.osaSetLogButton, self.osaRepeatButton)
        MainWindow.setTabOrder(self.osaRepeatButton, self.osaSweepButton)
        MainWindow.setTabOrder(self.osaSweepButton, self.osaSaveButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Z-Lab PIC Testing"))
        self.connectA.setText(_translate("MainWindow", "Connect"))
        self.connectLabel_a.setText(_translate("MainWindow", " A: not connected"))
        self.connectB.setText(_translate("MainWindow", "Connect"))
        self.connectLabel_b.setText(_translate("MainWindow", " B: not connected"))
        self.xDisplay_a.setText(_translate("MainWindow", "X: 0 V"))
        self.xGround_a.setText(_translate("MainWindow", "Ground"))
        self.yDisplay_a.setText(_translate("MainWindow", "Y: 0 V"))
        self.yGround_a.setText(_translate("MainWindow", "Ground"))
        self.zDisplay_a.setText(_translate("MainWindow", "Z: 0 V"))
        self.zGround_a.setText(_translate("MainWindow", "Ground"))
        self.yDisplay_b.setText(_translate("MainWindow", "Y: 0 V"))
        self.yGround_b.setText(_translate("MainWindow", "Ground"))
        self.xDisplay_b.setText(_translate("MainWindow", "X: 0 V"))
        self.xGround_b.setText(_translate("MainWindow", "Ground"))
        self.zDisplay_b.setText(_translate("MainWindow", "Z: 0 V"))
        self.zGround_b.setText(_translate("MainWindow", "Ground"))
        self.connectLabel_power.setText(_translate("MainWindow", " Meter: not connected"))
        self.connectPower.setText(_translate("MainWindow", "Connect"))
        self.powerDisplay.setText(_translate("MainWindow", "0.00"))
        self.lambdaLabel.setText(_translate("MainWindow", "λ:"))
        self.wavelengthApply.setText(_translate("MainWindow", "Apply"))
        self.groundAll_b.setText(_translate("MainWindow", "Ground All B"))
        self.groundAll_a.setText(_translate("MainWindow", "Ground All A"))
        self.groupBox_autoAlign.setTitle(_translate("MainWindow", "Auto Aligment"))
        self.label.setText(_translate("MainWindow", "Iterations:"))
        self.label_2.setText(_translate("MainWindow", "Tolerance:"))
        self.label_3.setText(_translate("MainWindow", "Time step:"))
        self.pushButton.setText(_translate("MainWindow", "Align A"))
        self.pushButton_2.setText(_translate("MainWindow", "Align B"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Piezo/Power"))
        self.osaRepeatButton.setText(_translate("MainWindow", "Repeat"))
        self.osaSweepButton.setText(_translate("MainWindow", "Single Sweep"))
        self.osaSweepButton.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.osaConnectButton.setText(_translate("MainWindow", "Connect"))
        self.groupBox.setTitle(_translate("MainWindow", "Window sweep"))
        self.numWindowsLabel.setText(_translate("MainWindow", "Windows:"))
        self.windowStartButton.setText(_translate("MainWindow", "Start"))
        self.saveDataCheckbox.setText(_translate("MainWindow", "Save data"))
        self.osaSetLinButton.setText(_translate("MainWindow", "Linear"))
        self.osaSetLinButton.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.osaSetLogButton.setText(_translate("MainWindow", "Log"))
        self.osaSetLogButton.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.osaSaveButton.setText(_translate("MainWindow", "Save"))
        self.osaSaveButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.printButton.setText(_translate("MainWindow", "Print"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.osaTab), _translate("MainWindow", "OSA"))
        self.addPlotButton.setText(_translate("MainWindow", "Add plot"))
        self.removePlotButton.setText(_translate("MainWindow", "Remove plot"))
        self.clearPlotButton.setText(_translate("MainWindow", "Clear all"))
        self.colorButton.setText(_translate("MainWindow", "Color"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.viewTab), _translate("MainWindow", "View Spectrum"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionpower_meter_setting.setText(_translate("MainWindow", "power meter setting"))
        self.actionOSA_settings.setText(_translate("MainWindow", "OSA settings"))
        self.actionview_COM_ports.setText(_translate("MainWindow", "piezo stage settings"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())