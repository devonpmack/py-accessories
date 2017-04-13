# Written by Devon Mack April 2017
# This class can be used to easily store variables to a file and load them back later

import json


class SaveLoad(object):
    def __init__(self, file_name=str()):
        try:
            if len(file_name) > 0:
                with open(file_name) as f:
                    self.__dict__ = json.load(f)
        except FileNotFoundError:
            print("[SaveLoad Error] Can't find file " + file_name + "!")

    def dump(self, file_name):
        f = open(file_name, "w")
        json.dump(self.__dict__, f, sort_keys=True, indent=4, separators=(',', ': '))

    def load(self, file_name):
        try:
            f = open(file_name, "r")
            self.__dict__ = json.load(f)
        except FileNotFoundError:
            print("[SaveLoad Error] Can't find file " + file_name + "!")
