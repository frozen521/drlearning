from pyqttutor.test import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class myForm(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myForm,self).__init__()
        self.setupUi(self)



if __name__=="__main__":
    app=QApplication(sys.argv)
    win=myForm()
    win.show()
    sys.exit(app.exec_())
