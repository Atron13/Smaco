import sys
import time
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
        self.entervalue.clicked.connect(self.inputload)
        self.runeveryid.clicked.connect(self.run)
        self.label_5.setText(">>>")
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)

    def inputload(self):
        finput=self.entervalueid.text()
        self.datashowlabel.setText(">>> input file name is loaded")
        self.label_5.setText(">>>")
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.datashowlabel.setAlignment(QtCore.Qt.AlignLeft)
        global inputfile
        try:
            inputfile=open(finput,'r')
        except:
            print("file not found")
            self.datashowlabel.setText(">>> input file name is not loaded")
            self.label_5.setText(">>>")
            self.label_5.setAlignment(QtCore.Qt.AlignLeft)
            self.datashowlabel.setAlignment(QtCore.Qt.AlignLeft)
        else:
            i=0
            for each in inputfile:
                infile[i]=each
                #print(each)
                i=i+1
        


    def run(self):
        intr=0
        global reg
        reg=[0]*1000
        self.datashowlabel.setText(">>> run segment started in execution")
        self.label_5.setText(">>>")
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.datashowlabel.setAlignment(QtCore.Qt.AlignLeft)
        number=self.numbercommndsid.value()
        for i in range(number):
            temp=int(mem[i])
            opc=((temp)//(10000))
            temp=int(mem[i])%10000
            op1 =((temp)//(1000-1))
            temp=int(mem[i])
            op2 =((temp)%1000)
            if opc == 9:
                mem[op2]=infile[intr]
                intr=intr+1
                
            elif opc== 4:#MOVER
                reg[op1]=mem[op2]
                
            elif opc== 5:#MOVEM
                mem[op2]=reg[op1]
                
            elif opc==1:#ADD
                reg[op1]=reg[op1]+mem[op2]

            elif opc== 2:#SUB
                reg[op1]=reg[op1]-mem[op2]

            elif opc==10:#PRINT
                self.datashowlabel.setText("value is "+mem[op2])

            elif opc==0:#STOP
                print("stoped")
            
                



    def commands(self):
        global mem
        global infile
        number=self.numbercommndsid.value()
        infile=[0]*10
        mem=[0]*1000
        fname=self.loadcommandfileid.text()
        self.datashowlabel.setText(">>> command file name is loaded")
        self.label_5.setText(">>>")
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.datashowlabel.setAlignment(QtCore.Qt.AlignLeft)
        global file
        try:
            file=open(fname,'r')
        except:
            print("file not found")
            self.datashowlabel.setText(">>> command file name is not loaded")
            self.label_5.setText(">>>")
            self.label_5.setAlignment(QtCore.Qt.AlignLeft)
            self.datashowlabel.setAlignment(QtCore.Qt.AlignLeft)
        else:
            i=0
            check=0
            for each in file:
                mem[i]=each
                i=i+1
                check=check+1
            if check == number:
                print("yes same")
            else:
                print("number of commands are less than the file commands")
                self.datashowlabel.setText(">>> number of commands are less than the file commands")
                self.label_5.setText(">>>")
                self.label_5.setAlignment(QtCore.Qt.AlignLeft)
                self.datashowlabel.setAlignment(QtCore.Qt.AlignLeft)


    def numberofcommands(self):
    	global number
    	number=self.numbercommndsid.value()
    	self.datashowlabel.setText(">>> number of commands entered")

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



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()