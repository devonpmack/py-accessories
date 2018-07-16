import sys


class LoadingBar(object):
    def __init__(self, width):
        """
        Initialize the LoadingBar instance.
        :param width: Width of the loading bar (# characters)
        """
        self.num_bars = width-2
        self.percent = 0

    def update(self, new_percent):
        """
        Update the LoadingBar and draw it to the screen
        :param new_percent: fraction of the loading bar that should be filled (0 to 1)
        """
        self.percent = new_percent
        left = round(self.percent * self.num_bars)
        right = self.num_bars - left
        text = "\r|%s%s| (%0.2f%% complete)" % (left * "=", right * "_", self.percent * 100)
        sys.stdout.write(text)
        sys.stdout.flush()