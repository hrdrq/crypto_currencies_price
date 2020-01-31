# -*- coding: utf-8 -*-
import time
from datetime import datetime

import pandas as pd
import requests

URL = 'https://coincheck.com/api/charts/candle_rates'

def get_data(pair, count, unit=3600):
    params = {
        'pair': pair,
        'limit': count,
        'unit': unit,
        'market': 'coincheck' 
    }
    res = requests.get(URL, params=params).json()
    result = [{
        'time': r[0],
        'open': r[1],
        'high': r[2],
        'low': r[3],
        'close': r[4],
        'volume': r[5]
    } for r in res]
    return list(reversed(result))

