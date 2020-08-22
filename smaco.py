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
        self.runeveryid.clicked.connect(self.run)


    def run(self):
        for i in range(number):
            opc=(mem[i])//(10000)
            op1 = (mem[i]%10000)//(1000-1)
            op2 = (mem[i]%1000)
            print(opc)
            print(op1)
            print(op2)


    def commands(self):
        global mem
        mem=[0]*number
        fname=self.loadcommandfileid.text()
        self.datashowlabel.setText("file name is loaded")
        self.datashowlabel.setAlignment(QtCore.Qt.AlignCenter)
        global file
        try:
            file=open(fname,'r')
        except:
            print("file not found")
            self.datashowlabel.setText("file name is not loaded")
            self.datashowlabel.setAlignment(QtCore.Qt.AlignCenter)
        else:
            #print("value of file")
            i=0
            for each in file:
                mem[i]=each
                print(each)
                i=i+1

            for i in range(len(mem)):
                print(mem[i])



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