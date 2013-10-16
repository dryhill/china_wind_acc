# -*- coding: utf-8 -*-

"""
Module implementing select_method.
"""
import sys
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from Ui_select_methon import Ui_Dialog
from Ui_wac_qg import Ui_acc_qg
from wac_qg import Acc_qg

class select_method(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.pb_qg.clicked.connect(self.pb_qg_clicked)     
        self.pb_sh.clicked.connect(self.pb_sh_clicked)            
    

    def pb_qg_clicked(self):
        """
        Slot documentation goes here.
        """
#        QtGui.QMessageBox.about(self,"测试","点击弹出窗口成功")
        ui1=Acc_qg()
        ui1.show()

    

    def pb_sh_clicked(self):
        """
        Slot documentation goes here.
        """
        QtGui.QMessageBox.about(self,"测试","点击弹出窗口成功")
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)    
    ui=select_method()
    ui.show()
    sys.exit(app.exec_())
