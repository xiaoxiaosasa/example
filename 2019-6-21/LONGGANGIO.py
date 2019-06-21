# -*- coding: UTF-8 -*-
# author:yuliang
import time
from threading import RLock,Thread
import serial
#龙岗IO
class LongGangIO(Thread):
    def __init__(self,COM):
        Thread.__init__(self)
        self.com = COM
        self.IN_STATUS = {}
        self.isRunning =False
        self.serialPortLock=RLock()
        self.initIO()

    def initIO(self):
        try:
            self.BoardSerial = serial.Serial(port=self.com,baudrate=9600,timeout=2)
            self.BoardSerial.setRTS(False)
            self.isRunning=True
            self.start()
        except:
            import traceback
            traceback.print_exc()

    def run(self):
        while self.isRunning:
            self.getSTATUS()

    def getSTATUS(self):
        self.serialPortLock.acquire()
        try:
            self.BoardSerial.write(bytearray([0x00,0x5A,0x56,0x00,0x07,0x00,0x00,0x00,0xB7]))
            res = self.BoardSerial.read(9)
        except Exception as e:
            print(e)
        finally:
            self.serialPortLock.release()
        if res=='':return
        if res[-1]!=self.checkSum(res[:-1]):
            print('CHECKSUM ERROR')
            return

        if res:
            stat=res[7]
            print(stat,type(stat),type(res),res)
            mask=0b00000001
            for i in range(8):
                self.IN_STATUS[i]=bool(stat&mask)
                mask=mask<<1
        print(self.IN_STATUS)

    def checkSum(self,fram):
        sum=0
        for i in fram:
            if type(i)==str:
                sum+=ord(i)
            else:
                sum+=i
        return sum%256

    def __getitem__(self, item):
        try:
            return self.IN_STATUS[item] if item in self.IN_STATUS else False
        finally:
            pass
    def __setitem__(self, key, value):
        CMD=[0x00,0x5A,0x56,0x00,None,None,0x00,0x00,None]

        CMD[4]= 0x01 if value else 0x02
        CMD[5]=key+1
        CMD[8]=self.checkSum(CMD[:-1])
        self.serialPortLock.acquire()
        try:
            self.BoardSerial.write(bytearray(CMD))
            self.BoardSerial.read(9)
        except Exception as e:
            print(e)
        finally:
            self.serialPortLock.release()



if __name__ == '__main__':
    ser=LongGangIO('com3')

    time.sleep(1)
    while ser.isRunning:
        ser[4]=1
        time.sleep(2)
        ser[4]=0
        time.sleep(2)

