from configuration import SERVER_HOST
from configuration import SERVER_PORT
import requests
from assertpy import assert_that


def test_1(set_up, some):
    print('test one')
    url = f"{SERVER_HOST}:{SERVER_PORT}/"

    with requests.get(url) as r:
        assert_that(r.status_code).is_equal_to(200)


def test_2(set_up, some):
    print('test two')
    url = f"{SERVER_HOST}:{SERVER_PORT}/user/1"

    with requests.get(url) as r:
        assert_that(r.status_code).is_equal_to(200)
