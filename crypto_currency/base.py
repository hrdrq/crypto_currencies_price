# -*- coding: utf-8 -*-
import os
from logging import Formatter, handlers, getLogger, StreamHandler, DEBUG

import pandas as pd

class Base(object):

    def __init__(self, name=None):
        name = name or self.__class__.__name__.rsplit('.', 1)[-1]
        logger = getLogger(name)
        if len(logger.handlers) == 0:
            logger.setLevel(DEBUG)
            formatter = Formatter('\033[32m[%(asctime)s][{}]\033[0m%(message)s'.format(name), "%y-%m-%d %H:%M:%S")
            handler = StreamHandler()
            handler.setLevel(DEBUG)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            self.logger = logger
        self.logger = logger

    @property
    def d(self):
        import pdb
        return pdb.set_trace

    def p(self, *text):
        if isinstance(text[0], pd.DataFrame):
            self.logger.info("\n" + str(text[0]))
        else:
            self.logger.info(" ".join([str(x) for x in text]))
