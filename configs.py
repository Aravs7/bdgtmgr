__author__ = 'A'


class Config:

    props = dict()

    def __init__(self):
        """ Loading all configs from config.properties files"""
        f = open("files/config.properties", 'r')
        for line in f:
            (key, val) = line.split("=")
            self.props[key.strip(" ")] = val.rstrip("\n").strip(" ")
        print(self.props)

c= Config()



