# Form implementation generated from reading ui file 'PiezoSettings.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PiezoSettings(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(500, 400)
        widget.setWindowTitle("")
        self.applyButton = QtWidgets.QPushButton(parent=widget)
        self.applyButton.setGeometry(QtCore.QRect(320, 360, 75, 23))
        self.applyButton.setObjectName("applyButton")
        self.cancelButton = QtWidgets.QPushButton(parent=widget)
        self.cancelButton.setGeometry(QtCore.QRect(410, 360, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.okButton = QtWidgets.QPushButton(parent=widget)
        self.okButton.setGeometry(QtCore.QRect(230, 360, 75, 23))
        self.okButton.setObjectName("okButton")
        self.label = QtWidgets.QLabel(parent=widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=widget)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 91, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.stageAPortLabel = QtWidgets.QLabel(parent=widget)
        self.stageAPortLabel.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.stageAPortLabel.setObjectName("stageAPortLabel")
        self.label_3 = QtWidgets.QLabel(parent=widget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_3.setObjectName("label_3")
        self.refreshPortsButton = QtWidgets.QPushButton(parent=widget)
        self.refreshPortsButton.setGeometry(QtCore.QRect(20, 120, 81, 23))
        self.refreshPortsButton.setObjectName("refreshPortsButton")
        self.StageAcombo = QtWidgets.QComboBox(parent=widget)
        self.StageAcombo.setGeometry(QtCore.QRect(90, 50, 171, 22))
        self.StageAcombo.setObjectName("StageAcombo")
        self.StageBcombo = QtWidgets.QComboBox(parent=widget)
        self.StageBcombo.setGeometry(QtCore.QRect(90, 80, 171, 22))
        self.StageBcombo.setObjectName("StageBcombo")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        self.applyButton.setText(_translate("widget", "Apply"))
        self.cancelButton.setText(_translate("widget", "Cancel"))
        self.okButton.setText(_translate("widget", "Ok"))
        self.label.setText(_translate("widget", "Piezo type:"))
        self.comboBox.setItemText(0, _translate("widget", "Thorlabs"))
        self.comboBox.setItemText(1, _translate("widget", "New Focus"))
        self.stageAPortLabel.setText(_translate("widget", "Stage A port:"))
        self.label_3.setText(_translate("widget", "Stage B port:"))
        self.refreshPortsButton.setText(_translate("widget", "Refresh ports"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_PiezoSettings()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec())
