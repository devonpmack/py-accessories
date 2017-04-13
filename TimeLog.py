import datetime as dt


class Timer(object):
    def __init__(self):
        self.start_time = dt.datetime.now()

    def time_str(self):
        return "[Elapsed time: %.2f] " % (dt.datetime.now() - self.start_time).total_seconds()

    def reset(self):
        self.start_time = dt.date.now()