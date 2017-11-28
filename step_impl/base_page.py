import logging
from getgauge.python import DataStoreFactory

class BasePage(object):

    def __init__(self, driver):
        print "initialized!"