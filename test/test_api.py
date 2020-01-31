# -*- coding: utf-8 -*-
import csv
import os
from datetime import datetime
import unittest
from unittest.mock import Mock, patch, PropertyMock

import pandas as pd
import vcr

from crypto_currency.api import get_data

class APITest(unittest.TestCase):

    def test_get_data(self):
        with vcr.use_cassette('test/vcr_cassettes/api.yaml'):
            res = get_data('btc_jpy', 240)
        print(res)
