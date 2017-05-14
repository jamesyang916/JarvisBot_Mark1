# coding: utf-8
import socket
import threading
import time
import webbrowser

class Jarvis_Connect(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.sock.settimeout(2)
        self._input = None
        self._output = None

    def initiate(self):
        self._input_stop = threading.Event()
        self._output_stop = threading.Event()
        self._input = threading.Thread(target=self.input_thr)
        self._output = threading.Thread(target=self.output_thr)

        self._input.start()
        self._output.start()

        self._input.join()
        self._output.join()

    def close(self):
        self.sock.close()

    def connect(self, IP, PORT):
        success = False
        try:
            self.sock.connect((IP,PORT))
            success = True
        except:
            raise
        return success

    def input_thr(self):
        while (not self._output_stop.is_set()):
            try:
                line = raw_input("")  
                self.sock.sendall(line)  # if clearance 1 granted, send encrypted(special delim + msg)

            except socket.error, e:
                if e[0] == 54:
                    print "Error: Jarvis has disconnected."
                    break
                else:
                    raise
                    break
            except:
                break
        self._input_stop.set()

    def output_thr(self):
        while (not self._input_stop.is_set()):
            try:
                res = self.sock.recv(1024)    
                if 'http' in res:
                    webbrowser.open(res)
                else:
                    print res
            except socket.timeout:
                pass                       
            except socket.error, e:
                if e[0] == 54:
                    print "Error: Jarvis has disconnected."
                break           
            except:
                break
        self._output_stop.set()

if __name__ == '__main__':
    #James iMac
    #IP = '100.8.233.176'
    #Columbia
    #IP = '160.39.140.121'
    #Virtual Machine
    IP = '40.71.102.0'
    PORT = 5002
    oJarv = Jarvis_Connect()
    try:
        success = oJarv.connect(IP, PORT)
        if success:   
            oJarv.initiate()
    except KeyboardInterrupt:
        print "Interrupted"
    except:
        oJarv.close()
        time.sleep(1)
        

