#encoding:utf-8
'''
Created on 2015-3-6
日志框（界面及逻辑）
@author: user
'''
from PyQt4.QtGui import QMessageBox
from PyQt4 import QtCore, QtGui, uic
from PyQt4.Qt import pyqtSlot
import logging
import time

logger = logging.getLogger()

class LogUi:
    '''日志框'''
    def __init__(self,logListView):
        self.logListView = logListView
        self.qi = QtGui.QStandardItemModel()
        logListView.setModel(self.qi)

    @staticmethod
    def now():
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
    def log(self,message):
        logger.info(message)
        logMessage = LogUi.now()+"\t"+message
        logItem = QtGui.QStandardItem(logMessage)
        if u'失败' in message or u'不通过' in message or u'离线' in message:
            logItem.setForeground(QtGui.QBrush(QtCore.Qt.red))
        elif u'终止' in message:
            logItem.setForeground(QtGui.QBrush(QtCore.Qt.blue))
        elif u'成功' in message:
            logItem.setForeground(QtGui.QBrush(QtCore.Qt.green))
        elif u'正常' in message:
            logItem.setForeground(QtGui.QBrush(QtCore.Qt.green))
        logItem.setEditable(False)
        self.qi.appendRow(logItem)
        if self.qi.rowCount() >= 100:
            self.qi.removeRow(0)
        self.logListView.scrollToBottom()

