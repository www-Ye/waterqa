
# -*- coding: utf-8 -*-
 
"""
PyQt5 tutorial 
 
In this example, we determine the event sender
object.
 
author: py40.com
last edited: 2017年3月
"""
 
import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication, QPushButton)
from PyQt5.QtGui import QIcon
import method as mt
 
global m, n, x, t, k, s, s0

class Example(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        btn1 = QPushButton("监测数据", self)
        btn1.move(30, 50)
 
        btn2 = QPushButton("标准数据", self)
        btn2.move(150, 50)
      
        btn3 = QPushButton("灰关联", self)
        btn3.move(270, 50)
        
        btn4 = QPushButton("未确知", self)
        btn4.move(390, 50)
        
        btn5 = QPushButton("模糊", self)
        btn5.move(510, 50)
        
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)
        btn4.clicked.connect(self.buttonClicked)
        btn5.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Event sender')
        self.show()
        
        
    def buttonClicked(self):
        global m, n, x, t, k, s, s0
        sender = self.sender()
        if(sender.text() == '监测数据'):
            m, n, x = self.showDialog()
            print(m, n)
            print(x)
        elif(sender.text() == '标准数据'):
            k, t, s = self.showDialog()
            s0 = s.T
            print(t, k)
            print(s0)
        elif(sender.text() == '灰关联'):
            ans = mt.Gray_Relational_Analysis(m, n, k, x, s0)
            print("灰关联")
            print(ans)
        elif(sender.text() == '未确知'):
            ans = mt.Unascertained_Measure_Model(m, n, k, x, s0)
            print("未确知")
            print(ans)
        elif(sender.text() == '模糊'):
            ans = mt.Fuzzy_Comprehensive_Evaluation(m, n, k, x, s0)
            print("模糊")
            print(ans)
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
    def showDialog(self):
 
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
 
        if fname[0]:
            x0 = pd.read_excel(fname[0])
            a = x0.shape[0]
            b = x0.shape[1] - 1
            c = x0.iloc[0:a, 1:b+1].values
            #with f:
            
            d = c[1][1]
            #self.textEdit.setText(d)  
            return a, b, c
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())