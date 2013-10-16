# -*- coding: utf-8 -*-

"""
Module implementing Acc_sh.
"""
import os
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from Ui_wac_sh import Ui_acc_sh


class Acc_sh(QDialog, Ui_acc_sh):
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
        
        self.le_us.textChanged[str].connect(self.leuschanged)
        self.le_w0.textChanged[str].connect(self.lew0changed)
        self.le_xi.textChanged[str].connect(self.lexichanged)
        self.le_nu.textChanged[str].connect(self.lenuchanged)
        self.le_h.textChanged[str].connect(self.lehchanged)
        self.le_b.textChanged[str].connect(self.lebchanged)
        self.le_l.textChanged[str].connect(self.lelchanged)
        self.le_m.textChanged[str].connect(self.lemchanged)
        self.le_hfznb.textChanged[str].connect(self.lehfznbchanged)
        self.le_hft.textChanged[str].connect(self.lehftchanged)
        
        self.btnyes.clicked.connect(self.calc)


    def leuschanged(self, text):        
        self.us=text
    def lew0changed(self, text):        
        self.w0=text
    def lexichanged(self, text):        
        self.xi=text
    def lenuchanged(self, text):        
        self.nu=text
    def lehchanged(self, text):        
        self.h=text
    def lebchanged(self, text):        
        self.b=text
    def lelchanged(self, text):        
        self.l=text
    def lemchanged(self, text):        
        self.m=text
    def lehfznbchanged(self, text):        
        self.hfznb=text
    def lehftchanged(self, text):        
        self.hft=text




    def calc(self):
#        print(self.us, self.ur, self.w0, self.xi, self.nu, self.h, self.b, self.l, self.m)
        self.sfacc=float(self.xi)*float(self.nu)*float(self.us)*float(self.w0)*float(self.h)*float(self.b)/float(self.m)
        self.le_sf.setText(str('{0:.3f}'.format(self.sfacc)))        
        height=(5, 10, 15, 20,30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550)
        uza=(1.09,1.28,1.42,1.52,1.67,1.79,1.89,1.97,2.05,2.12,2.18,2.23,2.46,2.64,2.78,2.91,2.91,2.91,2.91,2.91,2.91)
        uzb=(1.00,1.00,1.13,1.23,1.39,1.52,1.62,1.71,1.79,1.87,1.93,2.00,2.25,2.46,2.63,2.77,2.91,2.91,2.91,2.91,2.91)
        uzc=(0.65,0.65,0.65,0.74,0.88,1.00,1.10,1.20,1.28,1.36,1.43,1.50,1.79,2.03,2.24,2.43,2.60,2.76,2.91,2.91,2.91)
        uzd=(0.45,0.45,0.45,0.45,0.45,0.54,0.63,0.70,0.78,0.85,0.91,0.98,1.26,1.52,1.75,1.97,2.18,2.37,2.56,2.73,2.91)
        ccd=self.cb_ccd.currentText()
        
#        print(ccd, self.h)
       
        i=0
        while (float(self.h) > height[i] ):
            i=i+1

        if ccd=='A':
            self.uz=(uza[i]*(float(self.h)-height[i-1])+uza[i-1]*(height[i]-float(self.h)))/(height[i]-height[i-1])
        if ccd=='B':
            self.uz=(uzb[i]*(float(self.h)-height[i-1])+uzb[i-1]*(height[i]-float(self.h)))/(height[i]-height[i-1]) 
        if ccd=='C':
            self.uz=(uzc[i]*(float(self.h)-height[i-1])+uzc[i-1]*(height[i]-float(self.h)))/(height[i]-height[i-1])
        if ccd=='D':
            self.uz=(uzd[i]*(float(self.h)-height[i-1])+uzd[i-1]*(height[i]-float(self.h)))/(height[i]-height[i-1])

        vnm=40.0*(self.uz*float(self.us)*float(self.w0))**0.5
        gbavg=float(self.m)*10.0/float(self.h)/float(self.b)/float(self.l)
        
        
        br=(vnm*float(self.hft)/(float(self.b)*float(self.l))**0.5)**3.3*2.05*0.0001
        atr=br/(float(self.hft)**2)*(float(self.b)*float(self.l))**0.5/gbavg/(float(self.xi)**0.5)
        
        self.le_hf.setText(str('{0:.3f}'.format(atr)))
        
        f=open('acc.txt', 'w')
        f.write('依据规范《高层民用建筑钢结构技术规程》 JGJ 99-98')
        f.write(os.linesep)
        f.write('风压高度变化系数依据规范《建筑结构荷载规范》GB 50009-2010')
        f.write(os.linesep)
        f.write('体型系数'.ljust(15)+'{0:10.3f}'.format(float(self.us)))
        f.write(os.linesep)
        f.write('重现期调整系数'.ljust(15)+'{0:10.3f}'.format(float(self.ur)))      
        f.write(os.linesep)        
        f.write('基本风压(kn/M^2)'.ljust(15)+'{0:10.3f}'.format(float(self.w0))) 
        f.write(os.linesep)
        f.write('脉动增大系数'.ljust(15)+'{0:10.3f}'.format(float(self.xi)))   
        f.write(os.linesep)        
        f.write('脉动影响系数'.ljust(15)+'{0:10.3f}'.format(float(self.nu)))        
        f.write(os.linesep)        
        f.write('建筑物高度'.ljust(15)+'{0:10.3f}'.format(float(self.h)))
        f.write(os.linesep)        
        f.write('建筑物迎风宽度'.ljust(15)+'{0:10.3f}'.format(float(self.b)))
        f.write(os.linesep)        
        f.write('建筑物顺风向长度'.ljust(15)+'{0:10.3f}'.format(float(self.l)))
        f.write(os.linesep)        
        f.write('建筑物总质量(t)'.ljust(15)+'{0:10.3f}'.format(float(self.m)))
        f.write(os.linesep)        
        f.write('地面粗糙度类别'.ljust(15)+'{}'.rjust(10).format(ccd))
        f.write(os.linesep)        
        f.write('横风向临界阻尼比'.ljust(15)+'{0:10.3f}'.format(float(self.hfznb)))
        f.write(os.linesep)        
        f.write('横风向第一自振周期(s)'.ljust(15)+'{0:10.3f}'.format(float(self.hft)))
        f.write(os.linesep)        
        f.write(os.linesep)   
        f.write('计算过程中变量：')
        f.write(os.linesep)     
        f.write('风压高度变化系数'.ljust(15)+'{0:10.3f}'.format(self.uz))
        f.write(os.linesep)   
        f.write('顶点平均风速'.ljust(15)+'{0:10.3f}'.format(vnm))
        f.write(os.linesep)          
        f.write('横风向br'.ljust(15)+'{0:10.3f}'.format(br))
        f.write(os.linesep) 
        f.write('建筑物所受平均重力(kN/m^3)'.ljust(15)+'{0:10.3f}'.format(gbavg))
        f.write(os.linesep)         
        f.write('顺风向最大加速度'.ljust(15)+'{0:10.3f}'.format(self.sfacc))
        f.write(os.linesep) 
        f.write('横风向最大加速度'.ljust(15)+'{0:10.3f}'.format(atr))
        f.write(os.linesep) 
        f.close
        
#        print(self.uz, height[i-1], height[i], uza[i-1], uza[i])
#        print(uza[i]*(float(self.h)-height[i-1])+uza[i-1]*((height[i])-float(self.h)), height[i]-height[i-1])
#        print(float(self.h)-height[i-1], height[i]-float(self.h))
#        print(repr(vnm).ljust(6),repr(gbavg).ljust(6), repr(br).ljust(6), repr(atr).ljust(6), end=' ')
#        print(repr(2).ljust(6),repr(3).ljust(6), repr(4).ljust(6), repr(5).ljust(6), end=' ')


if __name__ == "__main__":
    import sys
    from PyQt4 import QtGui 
    app = QtGui.QApplication(sys.argv)    
    ui=Acc_sh()
    ui.show()
    sys.exit(app.exec_())

