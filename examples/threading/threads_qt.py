import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor

class Ui_Form(object):
    
    def setUI(self, Form):
        Form.setObjectName('Form')
        Form.resize(453, 408)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName('vertical Layout')
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName('vertical Layout 2')
        
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName('Text Browser')
        self.verticalLayout_2.addWidget(self.textBrowser)
        
        self.verticalLayout.addLayout(self.verticalLayout_2)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontal Layout')
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, 
                                           QtWidgets.QSizePolicy.Expanding, 
                                           QtWidgets.QSizePolicy.Minimum)
        
        self.horizontalLayout.addItem(spacerItem)
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("push button")
        self.horizontalLayout.addWidget(self.pushButton)
        
        spacerIte1 = QtWidgets.QSpacerItem(40, 20, 
                                           QtWidgets.QSizePolicy.Expanding, 
                                           QtWidgets.QSizePolicy.Minimum)
        
        self.horizontalLayout.addItem(spacerIte1)
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.retranslateUI(Form)
        
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
    def retranslateUI(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Example"))
        self.pushButton.setText(_translate("Form", "Input"))
        

class BrowserHandler(QtCore.QObject):
    
    running = False
    newTextAndColor = QtCore.pyqtSignal(str, object)
    
    def run(self):
        
        while True:
            self.newTextAndColor.emit(
                '{} - thread 2 variant 1.\n'.format(
                    str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))),
                QColor(0, 0, 255))
            
            QtCore.QThread.msleep(1000)
            
            self.newTextAndColor.emit(
                '{} - thread 2 variant 2.\n'.format(
                    str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))),
                QColor(255, 0, 0))
            
            QtCore.QThread.msleep(1000)
            
class MyWindow(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__()
        self.ui = Ui_Form()
        
        self.ui.setUI(self)
        
        self.ui.pushButton.clicked.connect(self.addAnotherTextAndColor)
        
        self.thread = QtCore.QThread()
        self.browserHandler = BrowserHandler()
        
        self.browserHandler.moveToThread(self.thread)
        
        self.browserHandler.newTextAndColor.connect(self.addNewTextAndColor)
        
        self.thread.started.connect(self.browserHandler.run)
        
        self.thread.start()
        
    @QtCore.pyqtSlot(str, object)
    def addNewTextAndColor(self, string, color):
        self.ui.textBrowser.setTextColor(color)
        self.ui.textBrowser.append(string)
        
    def addAnotherTextAndColor(self):
        self.ui.textBrowser.setTextColor(QColor(0, 255, 0))
        self.ui.textBrowser.append('{} - thread 2 variant 3.\n'.format(
            str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))))
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
        