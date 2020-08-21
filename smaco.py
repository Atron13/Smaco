import sys
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore,QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("smaco.ui", self)

        self.activate.clicked.connect(self.activating)
        self.deactivate.clicked.connect(self.deactivating)
        self.numbercommands.clicked.connect(self.numberofcommands)
        self.loadcommands.clicked.connect(self.commands)


    def enterdata(self,i):
    	mem[i]=self.loadcommandsid.value()
    	self.loadcommands.clicked.connect()


    def commands(self,i):
    	global mem
    	mem=[0]*10000
    	for i in range(number):
    		enterdata(self,i)
    	self.datashowlabel.setText("data entered for ")
    	self.datashowlabel.setAlignment(QtCore.Qt.AlignCenter)

    	for i in range(number):
    		print(mem[i])


    def enterdata(self,i):
    	mem[i]=self.loadcommandsid.value()
    	self.loadcommands.clicked.connect()


    def numberofcommands(self):
    	global number
    	number=self.numbercommndsid.value()
    	self.datashowlabel.setText("number of commands entered")
    	self.datashowlabel.setAlignment(QtCore.Qt.AlignCenter)

    def activating(self):
    	self.labelforactivate.setText("Activate")
    	self.labelforactivate.setStyleSheet("Color:limegreen;font-weight:bold")#mediumseagreen green
    	self.labelforactivate.setAlignment(QtCore.Qt.AlignCenter)
    	self.datashowlabel.setText("System is Activated Enter Number of commands")
    	self.datashowlabel.setAlignment(QtCore.Qt.AlignCenter)

    def deactivating(self):
    	self.labelforactivate.setText("Deactivate")
    	self.labelforactivate.setStyleSheet("Color:red;")
    	self.labelforactivate.setAlignment(QtCore.Qt.AlignCenter)
	#def deactivating(self):
		#self.labelforactivate.setText("Deactivate")



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()