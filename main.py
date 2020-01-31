# -*- coding: utf-8 -*-

from crypto_currency.base import Base
from crypto_currency.data import Data
from crypto_currency.chart import Chart
from crypto_currency import slack

def main():
    data = Data()
    chart = Chart()
    chart.update_subplot(data.pairs_candles)
    image_bytes = chart.to_bytes()
    slack.file('times_son', image_bytes)
    
if __name__ == '__main__':
    main()
