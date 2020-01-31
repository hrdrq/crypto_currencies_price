# -*- coding: utf-8 -*-
import io

import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib import ticker
from matplotlib.gridspec import GridSpec
from matplotlib import colors as mcolors
from matplotlib.collections import LineCollection, PolyCollection

from crypto_currency.base import Base

plt.style.use('dark_background')
LABEL_FORMAT = '%y-%m-%d\n%H:%M' # '%y%m%d %H:%M'

NROWS = 4
NCOLS = 3

class Chart(Base):

    def __init__(self, fig_w=24, fig_h=16):
        super().__init__()
        self.fig_w = fig_w
        self.fig_h = fig_h
        self.fig, self.axes = plt.subplots(NROWS, NCOLS, figsize=(fig_w, fig_h))
        # plt.tight_layout()

    def to_bytes(self):
        sio = io.BytesIO()
        self.save_file(sio)
        return sio.getvalue()

    def save_file(self, target):
        file_format = 'png'
        self.fig.savefig(target, format=file_format)

    def update_subplot(self, pairs_candles):
        total = len(pairs_candles)
        p = 0
        for i in range(NROWS):
            for j in range(NCOLS):
                ax = self.axes[i, j]
                pair_candles = pairs_candles[p]
                price = pair_candles['candles']['close'].iat[-1]
                self.add_candles(ax, pair_candles['candles'])
                self.add_info(ax, pair_candles['pair_name'].upper(), price)
                p += 1
                if p == total:
                    break
        self.fig.canvas.draw()

    def add_candles(self, ax, candles, candle_width=0.6):
        line_collection, bar_collection = mpf.candlestick2_ohlc(
            ax,
            opens=candles['open'].values,
            closes=candles['close'].values,
            lows=candles['low'].values,
            highs=candles['high'].values,
            width=candle_width,
            colorup='g',
            colordown='r',
            alpha=1
        )
        def formatter(x, pos):
            try:
                return candles['time'][int(x)].strftime(LABEL_FORMAT)
            except (IndexError, KeyError):
                return ''

        ax.xaxis.set_major_formatter(ticker.FuncFormatter(formatter))

    def add_info(self, ax, pair_name, price):
        _, y_max = ax.get_ybound()
        x_min, _ = ax.get_xbound()
        price_str = str(round(price, 2))
        ax.text(x_min, y_max, pair_name + " " + price_str, size=20,
             ha="left", va="top",
             bbox=dict(boxstyle="round",
                       ec='blue',
                       fc='darkblue',
                       )
             )

