import socket
from threading import Thread,RLock
from _thread import start_new_thread
class DevServer(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.addr =(ip,port)
        self.isRunning = True
        self.conn = None

    def start(self):
        self.sock = socket.socket()
        self.sock.bind(self.addr)
        self.sock.listen(5)
        Thread.start(self)

    def ThreadFun(self,conn):
        try:
            while True:
                data = conn.recv(1024)
                if not data:continue
                print('接受：',data.decode('utf-8'))
                rtn = self.__process(data.strip())
                if rtn is not None: conn.send(rtn)
                print('已返回')
        except Exception:
            conn.close()

    def run(self):
        while self.isRunning:
            try:
                conn,addr = self.sock.accept()
                print(addr)
                start_new_thread(self.ThreadFun,(conn,))
            except Exception as e:
                import traceback
                traceback.print_exc()

    def __process(self,data):
        return data

if __name__ == '__main__':
    server = DevServer('192.168.18.100',8000)
    server.start()
    # server = DevServer('192.168.10.6', 8000)
    # server.start()

