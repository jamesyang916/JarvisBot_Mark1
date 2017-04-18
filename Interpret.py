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
    def __init__(self):
        self.options = {
            "who are you" : self.name,
            "jarvis" : self.sir, 
            "what day is it today" : self.day,
            "hi" : self.greet,
            "do you like spam" : self.spam,
            "do you love me" : self.love,
            }
        pass

    def name(self):
        return "I am Jarvis."
    def sir(self):
        return "Yes?"
    def day(self):
        my_date = date.today()
        return calendar.day_name[my_date.weekday()]
    def greet(self):
        return "Hello."
    def spam(self):
        return "I love spam too much."
    def love(self):
        return "I am not supposed to feel, but yes I do."
    def interpret(self, Msg): 
        msg = Msg.getMsg().lower().translate(None, string.punctuation)
        try:
            res = self.options[msg]()
        except KeyError:
            res = 'No information.'
        return res


