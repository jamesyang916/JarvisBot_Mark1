import threading
import Message
import Queue

class Console(object):
    def __init__(self, oInterpret):
        self.oInterpret = oInterpret
        self.requests = Queue.Queue()

    def addRequest(self, request):
        self.requests.put(request)

    def console(self):       
        ThreadInput = threading.Thread(target=self.cueInput)
        ThreadOutput = threading.Thread(target=self.cueOutput)
        ThreadInput.start()
        ThreadOutput.start()
        ThreadInput.join()
        ThreadOutput.join()

    def cueInput(self):
        _input = ''
        while 1:
            _input = raw_input("")
            request = Message.Message(_input)
            self.addRequest(request)

    def cueOutput(self):
        while 1:
            while not self.requests.empty():
                res = self.oInterpret.interpret(self.requests.get())
                # res = self.oInterpret.test(request, 'console')
                if res == None:
                    continue
                print res
        


