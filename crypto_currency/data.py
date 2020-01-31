# -*- coding: utf-8 -*-
from itertools import groupby
import threading

import pandas as pd

from crypto_currency.base import Base
from crypto_currency.constant import CANDLES_NUM, pairs
from crypto_currency import api

class Data(Base):

    def __init__(self):
        super().__init__()
        self.pairs_candles = []
        # def get(pair):
        #     print(pair)
        #     dict_data = api.get_data(pair, CANDLES_NUM)
        #     candles = pd.DataFrame.from_dict(dict_data)
        #     candles = util.format_candles(candles)
        #     self.pairs_candles.append(dict(pair_name=pair, candles=candles))
        # threads = [threading.Thread(target=get, args=(pair,)) for pair in pairs]
        # for thread in threads:
        #     thread.start()
        # for thread in threads:
        #     thread.join()
        #
        for pair in pairs:
            dict_data = api.get_data(pair, CANDLES_NUM)
            candles = pd.DataFrame.from_dict(dict_data)
            candles = self.format_candles(candles)
            self.pairs_candles.append(dict(pair_name=pair, candles=candles))

    @staticmethod
    def format_candles(candles):
        candles  = candles.astype({
            'open': 'float64',
            'low': 'float64',
            'high': 'float64',
            'close': 'float64',
            'volume': 'int'
        })
        candles['time'] = pd.to_datetime(candles['time'], unit='s')
        # candles['time'] = candles['time'].dt.tz_localize('Asia/Tokyo')
        candles['time'] = candles['time'].dt.tz_localize('utc').dt.tz_convert('Asia/Tokyo')
        return candles
