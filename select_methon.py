# -*- coding: utf-8 -*-

"""
Module implementing select_method.
"""
import atexit
import sys
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtGui

from Ui_select_methon import Ui_Dialog
from Ui_wac_qg import Ui_acc_qg
from wac_qg import Acc_qg
from wac_sh import Acc_sh

class Select_method(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pb_qg.clicked.connect(self.pb_qg_clicked)     
        self.pb_sh.clicked.connect(self.pb_sh_clicked)        
    
    @pyqtSignature("")
    def pb_qg_clicked(self):
        """
        Slot documentation goes here.
        """
        ui1=Acc_qg()
        ui1.exec_()
    
    @pyqtSignature("")
    def pb_sh_clicked(self):
        """
        Slot documentation goes here.
        """
        ui1=Acc_sh()
        ui1.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)    
    ui=Select_method()
    ui.show()
    sys.exit(app.exec_())
