import socket
import threading
from Queue import PriorityQueue

class Client(object):
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.thread = None
        self.requests = PriorityQueue(10)
        self.alive = True

    def sendto(self, msg):
        self.conn.send(msg)
    def recvfrom(self, bits):
        res = self.conn.recv(bits)
        return res
    def close(self):
        self.conn.close()
    def updateThread(self, thread):
        self.thread = thread
    def getThread(self):
        return self.thread
    def getAddr(self):
        return self.addr
    def addRequest(self, request):
        if not self.requests.full():
            self.requests.put(request)     
    def getRequest(self):
        if not self.empty():
            return self.requests.get()
        return None
    def empty(self):
        return self.requests.empty()
    def updateLife(self, boolean):
        self.alive = boolean
    def is_alive(self):
        return self.alive

        


