# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\PRO\china_wind_acc\select_methon.ui'
#
# Created: Thu Oct 17 01:55:17 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(374, 229)
        Dialog.setSizeGripEnabled(True)
        self.pb_qg = QtGui.QPushButton(Dialog)
        self.pb_qg.setGeometry(QtCore.QRect(60, 20, 231, 71))
        self.pb_qg.setObjectName(_fromUtf8("pb_qg"))
        self.pb_sh = QtGui.QPushButton(Dialog)
        self.pb_sh.setGeometry(QtCore.QRect(60, 120, 231, 71))
        self.pb_sh.setObjectName(_fromUtf8("pb_sh"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pb_qg.setText(_translate("Dialog", "依据全国规范", None))
        self.pb_sh.setText(_translate("Dialog", "依据上海高层钢结构规范", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

