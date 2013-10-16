# -*- coding: utf-8 -*-

"""
Module implementing Acc_sh.
"""
from math import exp, sqrt, log
import os
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_wac_sh import Ui_acc_sh

class Acc_sh(QDialog, Ui_acc_sh):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.le_us.textChanged[str].connect(self.leuschanged)
        self.le_w0.textChanged[str].connect(self.lew0changed)
        self.le_w.textChanged[str].connect(self.lewchanged)        
        self.le_xi.textChanged[str].connect(self.lexichanged)
        self.le_nu.textChanged[str].connect(self.lenuchanged)
        self.le_h.textChanged[str].connect(self.lehchanged)
        self.le_b.textChanged[str].connect(self.lebchanged)
        self.le_l.textChanged[str].connect(self.lelchanged)
        self.le_m.textChanged[str].connect(self.lemchanged)
        self.le_hfznb.textChanged[str].connect(self.lehfznbchanged)
        self.le_hft.textChanged[str].connect(self.lehftchanged)
        self.le_beta.textChanged[str].connect(self.lebetachanged)
        
        self.btnyes.clicked.connect(self.calc)
        
        self.us='0'
        self.ur='0'
        self.w='0'
        self.w0='0'
        self.xi='0'
        self.nu='0'
        self.h='1'
        self.b='0'
        self.l='0'
        self.m='1'
        self.hfznb='0'
        self.hft='1'
        self.beta='1'
        
    def leuschanged(self, text):        
        self.us=text
    def lew0changed(self, text):        
        self.w0=text
    def lewchanged(self, text):        
        self.w=text        
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
    def lebetachanged(self, text):        
        self.beta=text



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
            alpha=1.0
            aw=0.12
        if ccd=='B':
            self.uz=(uzb[i]*(float(self.h)-height[i-1])+uzb[i-1]*(height[i]-float(self.h)))/(height[i]-height[i-1]) 
            alpha=2.0
            aw=0.16
        if ccd=='C':
            self.uz=(uzc[i]*(float(self.h)-height[i-1])+uzc[i-1]*(height[i]-float(self.h)))/(height[i]-height[i-1])
            alpha=3.0
            aw=0.22
        if ccd=='D':
            self.uz=(uzd[i]*(float(self.h)-height[i-1])+uzd[i-1]*(height[i]-float(self.h)))/(height[i]-height[i-1])
            alpha=4.0
            aw=0.3
            
        #get heng xiang zhen fu
        storylevel=self.pte_h.toPlainText()
        list_storylevel=(str(storylevel).strip()).split()
        #get mass of storey
        storymass=self.pte_m.toPlainText()
        list_storymass=(str(storymass).strip()).split()
        
        print(list_storylevel)
        print(list_storymass)
        
        gr=sqrt(2*log(600*float(self.hft)))+0.5772/sqrt(2*log(600*float(self.hft)))
        
        #M1
        M1=0.0
        for i in range(len(list_storymass)):
            M1+=float(list_storymass[i])*(float(list_storymass[1])/float(self.h))**(2*float(self.beta))
        
        #theta_m
        if float(self.beta) >=1 :
            theta_m=(4*alpha+3)/(4*alpha+2*float(self.beta)+1)
        else:
            theta_m=(2*alpha+2)/(2*alpha+float(self.beta)+1)            
        
        #n1
        wh=self.uz*float(self.w0)
        uh=sqrt(1600*wh)
        n1=float(self.hft)*float(self.b)/uh
        
        #ahr,adb
        ahr=float(self.h)/sqrt(float(self.b)*float(self.l))
        adb=float(self.l)/float(self.b)
        
        #u
        u=uh/float(self.hft)/float(self.b)
        u=u/9.8
        
        #ztaa1
        ztaa1=(0.0025*(1-u*u)*u+0.000125*u*u)/(1-u*u+0.0291*u*u)
        
        #fp
        fp=10**(-5)*(191-9.48*aw+1.28*ahr+ahr*aw)*(68-21*adb+3*adb**3)
        
        #sp
        sp=(0.1*aw**(-0.4)-0.0004*exp(aw))*(0.84*ahr-2.12-0.05*ahr*ahr)*(0.422+adb**(-1)-0.08*adb**(-2))
        
        #bk
        bk=(1+0.00473*exp(1.7*aw))*(0.065+exp(1.26-0.63*ahr))*exp(1.7-3.44/adb)
        
        #gamma
        gamma=(-0.8+0.06*aw+0.0007*exp(aw))*(0-ahr**(0.34)+0.00006*exp(ahr))*(0.414*adb+1.67*adb**(-1.23))
        
        #sf
        sf=sp*bk*(n1/fp)**gamma/(
        (1-(n1/fp)**2)**2+bk*(n1/fp)**2
        )
        
        #!need check sf
        
        atr=gr*float(self.h)/M1*float(self.b)*wh*sqrt(
        3.14159*theta_m*abs(sf)/4.0/(float(self.hfznb)+ztaa1)
        )
        
        self.le_hf.setText(str('{0:.3f}'.format(atr)))
        
        f=open('acc.txt', 'w')
        f.write('依据规范《上海高层建筑钢结构设计规程》 DG/TJ08-32-2008')
        f.write(os.linesep)
        f.write('风压高度变化系数依据规范《建筑结构荷载规范》GB 50009-2010')
        f.write(os.linesep)
        f.write('体型系数'.ljust(15)+'{0:10.3f}'.format(float(self.us)))    
        f.write(os.linesep) 
        
        f.write('基本风压(kn/M^2)'.ljust(15)+'{0:10.3f}'.format(float(self.w0))) 
        f.write(os.linesep)
        f.write('10年重现期风压(kn/M^2)'.ljust(15)+'{0:10.3f}'.format(float(self.w))) 
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
        
        f.write('横风向一阶结构阻尼比'.ljust(15)+'{0:10.3f}'.format(float(self.hfznb)))
        f.write(os.linesep)        
        f.write('横风向第一自振周期(s)'.ljust(15)+'{0:10.3f}'.format(float(self.hft)))
        f.write(os.linesep)        
        f.write(os.linesep)   
        f.write('计算过程中变量：')
        f.write(os.linesep)     
        f.write('风压高度变化系数'.ljust(15)+'{0:10.3f}'.format(self.uz))
        
        f.write(os.linesep)     
        f.write('alpha'.ljust(15)+'{0:10.3f}'.format(alpha))        
        f.write(os.linesep)     
        f.write('a_w'.ljust(15)+'{0:10.3f}'.format(aw))  
        
        f.write(os.linesep)     
        f.write('g_R'.ljust(15)+'{0:10.3f}'.format(gr))   
        f.write(os.linesep)     
        f.write('M1'.ljust(15)+'{0:10.3f}'.format(M1))         
        f.write(os.linesep)     
        f.write('theta_m'.ljust(15)+'{0:10.3f}'.format(theta_m))  
        f.write(os.linesep)     
        f.write('wh'.ljust(15)+'{0:10.3f}'.format(wh))        
        f.write(os.linesep)     
        f.write('uh'.ljust(15)+'{0:10.3f}'.format(uh))      
        f.write(os.linesep)     
        f.write('n1'.ljust(15)+'{0:10.3f}'.format(n1))     
        f.write(os.linesep)     
        f.write('a_hr'.ljust(15)+'{0:10.3f}'.format(ahr))   
        f.write(os.linesep)     
        f.write('a_db'.ljust(15)+'{0:10.3f}'.format(adb))  
        f.write(os.linesep)     
        f.write('U'.ljust(15)+'{0:10.3f}'.format(u))       
        f.write(os.linesep)     
        f.write('zta_a1'.ljust(15)+'{0:10.3f}'.format(ztaa1))     
        f.write(os.linesep)     
        f.write('f_p'.ljust(15)+'{0:10.3f}'.format(fp))    
        f.write(os.linesep)     
        f.write('S_p'.ljust(15)+'{0:10.3f}'.format(sp))     
        f.write(os.linesep)     
        f.write('beta_k'.ljust(15)+'{0:10.3f}'.format(bk))          
        f.write(os.linesep)     
        f.write('gamma'.ljust(15)+'{0:10.3f}'.format(gamma))          
        f.write(os.linesep)     
        f.write('sf'.ljust(15)+'{0:10.3f}'.format(sf))          
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
