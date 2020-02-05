# -*- coding: utf-8 -*-
import argparse

from crypto_currency.base import Base
from crypto_currency.data import Data
from crypto_currency.chart import Chart
from crypto_currency import slack

def main(channel):
    data = Data()
    chart = Chart()
    chart.update_subplot(data.pairs_candles)
    image_bytes = chart.to_bytes()
    slack.file(channel, image_bytes)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('channel')
    a = parser.parse_args()
    main(a.channel)
