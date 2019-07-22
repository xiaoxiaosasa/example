import socket
import time


class Client:
    def __init__(self,ip,port):
        self.addr = (ip,port)
        self.client = socket.socket()
        self.client.settimeout(1)
        self.client.connect(self.addr)

    def cmd(self,req):
        try:
            self.client.send(req)
            time.sleep(0.05)
            while True:
                recvData = self.client.recv(1024)
                if not recvData:break
                print(recvData.decode('utf-8'))
        except Exception as e:
            print(e)



if __name__ == '__main__':
    client =Client('192.168.18.33',8000)
    while True:
        info = input("请输入>>")
        client.cmd(info.encode('utf-8'))