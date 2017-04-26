import datetime as dt
import re

class Timer(object):
    def __init__(self):
        self.start_time = dt.datetime.now()
        self.colour = None

    def time_str(self):
        if type(self.colour) is not str:
            return "[Elapsed time: %.2f] " % (dt.datetime.now() - self.start_time).total_seconds()
        else:
            return self.colour + "[Elapsed time: %.2f] " % (dt.datetime.now() - self.start_time).total_seconds() + \
                   "\033[0m"

    def reset(self):
        self.start_time = dt.datetime.now()

    def time_print(self, to_print):
        print(self.time_str() + to_print)

    def set_colour(self, colour=None):
        if 30 <= colour <= 37:
            self.colour = "\033[1;" + str(colour) + ";0m"
        elif colour is None:
            self.colour = None
        else:
            print("[Warning] Invalid colour!")