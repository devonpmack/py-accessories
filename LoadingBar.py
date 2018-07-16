import sys


class LoadingBar(object):
    def __init__(self, num_bars):
        self.num_bars = num_bars
        self.percent = 0

    def update(self, new_percent):
        self.percent = new_percent
        left = round(self.percent * self.num_bars)
        right = self.num_bars - left
        text = "\r|%s%s| (%0.2f%% complete)" % (left * "=", right * "_", self.percent * 100)
        sys.stdout.write(text)
        sys.stdout.flush()
