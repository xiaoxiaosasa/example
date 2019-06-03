#encoding:utf-8
"""
GPIO测试工具
@author:zws
"""

import pywinio
wio = pywinio.WinIO()


def read():
    while True:
        input("press ENTER to read status")
        vA00 = wio.get_port_byte(0xA00)
        vA02 = wio.get_port_byte(0xA02)
        
        pin1Value = vA00 & (0b01 << 1) != 0
        pin2Value = vA00 & (0b01 << 5) != 0
        pin3Value = vA00 & (0b01 << 6) != 0
        pin4Value = vA02 & (0b01 << 3) != 0
        print("pin1:%d\tpin2:%d\tpin3:%d\tpin4:%d"%(pin1Value,pin2Value,pin3Value,pin4Value))


pinAddMap = {6:(0xa02,5),7:(0xa03,7),8:(0xa05,4),9:(0xa05,5)}

def write():
    while True:
        cmd = input("press 6-9:1/0 to write ")
        pin,v = map(lambda x:int(x),cmd.split(":"))

        currentValue = wio.get_port_byte(pinAddMap[pin][0])
        if v == 0:
            currentValue &= (~(0b01 << pinAddMap[pin][1]))
        else:
            currentValue |= (0b01 << pinAddMap[pin][1])
            
        wio.set_port_byte(pinAddMap[pin][0],currentValue)
        
        
        
 def 

    

if __name__ == '__main__':
    #write()
    read()



