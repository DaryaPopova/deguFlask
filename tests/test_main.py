import pytest
import requests

import config
from tests.conftest import BaseTest


class TestMain(BaseTest):
    def test_1(self, set_up, some):
        print('test one')
        url = config.SERVER_HOST + ":" + str(config.SERVER_PORT)

        with requests.get(url) as r:
            print(r.text)

        self.assertEquals(r.status_code, 200)

    def test_2(self, set_up, some):
        print('test two')
