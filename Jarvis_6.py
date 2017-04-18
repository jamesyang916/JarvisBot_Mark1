# Jarvis_6
import threading
import Interpret
import Mobile

# Master Operator
class Jarvis(object):    
    # Jarvis Object Instantiation
    def __init__(self):
        self.oInterpret = None
        self.oMobile = None
        self.notifier = None

    def setup(self):
        print "Creating Interpret and Stream objects..."
        # Create Interpret Object
        self.oInterpret = Interpret.Interpret()
        # Create Stream Object
        self.oMobile = Mobile.Mobile(self.oInterpret)
        # Create Notifying Object
        self.notifier = threading.Thread(target=self.notify)
        # Wifi Control on Interpret and Output
        print "Task Completed."       

    def initiate(self):
        print 'Initiating objects...'
        # self.wifi_thr already started
        self.oMobile.mobile()
        self.notifier.start()
    def terminate(self):
        self.notifier.join()
    
    def notify(self):   # add clearance lvl distinction
        pass


        
    
        
   
        
        
        