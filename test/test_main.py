# -*- coding: utf-8 -*-
import csv
import os
from datetime import datetime
import unittest
from unittest.mock import Mock, patch, PropertyMock

import pandas as pd
import vcr

from main import main

now_str = datetime.now().strftime("%Y%m%d%H%M%S")
dir_str = 'test/res'
os.makedirs(dir_str, exist_ok=True)

file_i = 1
def mock_slack_file(channel, file):
    global file_i
    with open('{}/{}-{}-{}.png'.format(dir_str, now_str, channel, file_i), 'wb') as f:
        f.write(file)
    file_i += 1

class MainTest(unittest.TestCase):

    @patch('main.slack.file', mock_slack_file)
    def test_main(self):
        with vcr.use_cassette('test/vcr_cassettes/main.yaml'):
            main()
