def __manulAskDlg(self,title,msg,check):
	self.confirmDlg = QMessageBox()
	self.confirmDlg.setWindowTitle(title)
	self.confirmDlg.setIcon(QMessageBox.Question)
	self.confirmDlg.setText(self.__large(msg))
	self.confirmDlg.setParent(self)
	self.confirmDlg.setWindowFlags(QtCore.Qt.Dialog)
	
	if check == "check":
		self.confirmDlg.addButton("正常",QMessageBox.AcceptRole)
		self.confirmDlg.addButton("不正常",QMessageBox.RejectRole)
	elif check == "ok":
		self.confirmDlg.addButton("确定",QMessageBox.AcceptRole)
	elif check == "coonfirm":
		self.confirmDlg.addButton("是",QMessageBox.AcceptRole)
		self.confirmDlg.addButton("否",QMessageBox.RejectRole)
	self.manulDlgResult = self.confirmDlg.exec_()
	self.manulEvent.set()
	
def waitForManulCheckDlg():
	self.manulEvent.wait()
	self.manulEvent.clear()
	return self.manulDlgResult

def __manulAskDlgTrigger(self,result):
	if result == "NORMAL":
		self.confirmDlg.done(0)
	elif result =="ABNORMAL":
		self.confirmDlg.done(1)
