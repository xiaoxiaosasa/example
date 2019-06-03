# -*- coding: UTF-8 -*-
# author:yuliang
#data:2019.5.29
from threading import Thread,Condition
import time
cond = Condition()
products = 0
class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global products,cond
        while True:
            cond.acquire()
            if products < 10:
                products += 1
                time.sleep(1)
                print('producer(%s):produce one ,now %d products'% (self.name,products))
                cond.notify()
            else:
                print('producer(%s):already 10,stop produce ,now %d products'% (self.name,products))
                cond.wait()
            cond.release()


class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global products,cond
        while True:
            cond.acquire()
            if products > 0:
                products -= 1
                time.sleep(1)
                print('consumer(%s):consume one, now %d products'%(self.name,products))
            else:
                print('consumer(%s): no one to consume, now %d products'%(self.name,products))
                cond.wait()
            cond.release()



if __name__ == '__main__':
    for p in range(2):
        p = Producer()
        p.start()
    for c in range(2):
        c = Consumer()
        c.start()
