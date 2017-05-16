import socket
import threading
import Client
import Message

class Mobile(object):
    def __init__(self, oInterpret):
        self.oInterpret = oInterpret
        self.MAXCLIENTS = 2   # max number of clients
        self.MAXINTR = 10 # max number of interpreting threads
        self.clientlst = []
        self.clientthrlst = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        IP = ''
        PORT = 5002
        try:
            self.sock.bind((IP, PORT))
            self.sock.listen(10)

            self.run_event = threading.Event()
            self.run_event.set()
            self.Thread1 = threading.Thread(target=self.addClients)
        except socket.error as msg:
            print msg
   
    def addRequest(self, request):
        for client in self.clientlst:
            client.addRequest(request)
     
    def mobile(self):
        self.Thread1.start()
        try:
            while 1:
                time.sleep(2)
        except KeyboardInterrupt:
            print "KeyboardInterrupt Exception. Shutting down Jarvis."
            self.run_event.clear()
            self.Thread1.join()
            print "Main thread successfully closed."
        
    # Thread 1
    def addClients(self):
        while self.run_event.is_set():
            try:
                conn, addr = self.sock.accept()            
                client = Client.Client(conn, addr[0])
                print "Client %s has connected." %(client.getAddr())
                if len(self.clientlst) < self.MAXCLIENTS:               
                    self.clientlst.append(client)
                    thread = threading.Thread(target=self.connect, args=(client,))
                    thread.start() # this is funky
                    self.clientthrlst.append(thread)
                    client.updateThread(thread)
                else:
                    print 'Client %s has disconnected. Error: connection overload. Maximum clients reached.' %(client.getAddr())
                    client.close()
            except socket.error as msg:
                if msg[0] in [10053,10054,9]:  # if socket error raised
                    print 'Client %s has disconnected.' %(client.getAddr())
                client.close()
            time.sleep(1)
                         

    def delClient(self, client):
        self.clientlst.remove(client)
        self.clientthrlst.remove(client.getThread())
        client.close()

    # Thread 2
    def connect(self, client):
        ThreadInput = threading.Thread(target=self.queueInput, args=(client,))
        ThreadOutput = threading.Thread(target=self.queueOutput, args=(client,)) 
        ThreadInput.start()
        ThreadOutput.start()
        ThreadInput.join()
        ThreadOutput.join()
  
    def queueInput(self, client):
        _input = ''
        while 1:
            try:
                _input = client.recvfrom(1024)
                if _input == None:
                    raise socket.error(9)
                request = Message.Message(_input)
                client.addRequest(request)
            except socket.error as msg:
                if msg[0] in [10053,10054,9]:  # if socket error raised
                    print 'Client %s has disconnected.' %(client.getAddr())
                client.close()
                break
        self.delClient(client)
        client.updateLife(False)
    def queueOutput(self, client):
        while client.is_alive():
            while not client.empty():
                res = self.oInterpret.interpret(client.getRequest())
                # res = self.oInterpret.test(request, client.getAddr())  # interpret phase
                if res == None:
                    continue
                try:
                    client.sendto(res)
                except socket.error as msg:
                    continue
                    
        
    
                