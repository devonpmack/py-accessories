# Written by Devon Mack April 2017
# This class can be used to easily store variables to a file and load them back later

import json


class SaveLoad(object):
    def __init__(self, file_name="", create=False):
        if file_name != "":
            self.load(file_name, create)

    def dump(self, file_name):
        f = open(file_name, "w")
        json.dump(self.__dict__, f, sort_keys=True, indent=4, separators=(',', ': '))
        f.close()

    def load(self, file_name, create=False):
        try:
            f = open(file_name, "r")
            self.__dict__ = json.load(f)
            f.close()
        except FileNotFoundError:
            if create:
                print("[SaveLoad] Creating file " + file_name)
                f = open(file_name, "w")
                f.close()
            else:
                raise FileNotFoundError
