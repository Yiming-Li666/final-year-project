import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from EHR_Ctr import EHR_Ctr

class MainWindow(QMainWindow):
	# define signals
	record_Signal = pyqtSignal()
	quit_Signal = pyqtSignal()
	select_Signal = pyqtSignal()
	save_Signal = pyqtSignal()

	# intial
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		loadUi('EHR_UI.ui', self)
		self.set_ui()
		self.Button_Record.clicked.connect(self.emit_record_signal)
		self.Button_Quit.clicked.connect(self.emit_quit_signal)
		self.actionA.triggered.connect(self.emit_select_file)
		self.actionB.triggered.connect(self.emit_save_file)

	# Add placeholders of plainTextEdits
	def set_ui(self):
		self.plainTextEdit_Name.setPlaceholderText("请输入你的Name")
		self.plainTextEdit_ID.setPlaceholderText("请输入你的ID")
		self.plainTextEdit_Date.setPlaceholderText("请输入你的Date")
		self.plainTextEdit_Sympotom.setPlaceholderText("请输入你的Sympotom")
		self.plainTextEdit_Disease.setPlaceholderText("请输入你的Disease")
		self.plainTextEdit_Treatment.setPlaceholderText("请输入你的Treatment")
		self.plainTextEdit_WholeText.setPlaceholderText("Will display the whole recognized text.")
		self.EHR_Ctr = EHR_Ctr()
		self.EHR_Ctr.setCtr(self)

	# emit signal
	def emit_record_signal(self): 
		self.record_Signal.emit()
		
	def emit_quit_signal(self): 
		self.quit_Signal.emit()

	def emit_select_file(self):
		self.select_Signal.emit()

	def emit_save_file(self):
		self.save_Signal.emit()

app = QApplication(sys.argv)
mainwindow = MainWindow()
# Change the title of mainwindow
_translate = QtCore.QCoreApplication.translate
mainwindow.setWindowTitle(_translate("MainWindow", "EHR_Test"))

mainwindow.show()
sys.exit(app.exec())