# Input Interpreter
import string
from datetime import date
import calendar
class Interpret(object):
    # Wikipedia
    # Wolfram Q35XX4-9AG2KK3Q9L
    # last resort: Google Search API:
    # collect data from very first link: all sentences w/ highlighted words.
    # "..."\n(source1)\n"..."\n(source2)\n"
    def __init__(self,):
        self.options = {}
        self.buildDict()
    def buildDict(self,):
        with open('Database.txt') as f:
            for line in f:
                arr = line.split('$$')
                self.options[arr[0]] = arr[1]
            
    def interpret(self, Msg): 
        msg = Msg.getMsg().lower().translate(None, string.punctuation)
        try:
            res = self.options[msg]
        except KeyError:
            res = 'No information.'
        return res


