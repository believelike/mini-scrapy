# coding: utf8

""" Base Spider"""

from .conf.settings import Settings
from .http.request import Request


class Spider(object):

    """ Base Spider"""

    start_urls = []
    custom_settings = None

    def __init__(self):
        if not hasattr(self, "start_urls"):
            self.start_urls = []
        # init settings
        self.settings = Settings(self.custom_settings)

        self.initialize()

    def initialize(self):
        """ initialize """
        pass

    def start_requests(self):
        """ start_requests """
        for url in self.start_urls:
            yield Request(url)

    def parse(self):
        """ parse """
        raise NotImplementedError