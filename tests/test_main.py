import os

from flake8.api import legacy as flake8

from configuration import SERVER_HOST
from configuration import SERVER_PORT
import requests
from assertpy import assert_that


def test_1(set_up, some):
    print('test one')
    url = f"http://{SERVER_HOST}:{SERVER_PORT}/"

    with requests.get(url) as r:
        assert_that(r.status_code).is_equal_to(200)


def test_2(set_up, some):
    print('test two')
    url = f"http://{SERVER_HOST}:{SERVER_PORT}/user/1"

    with requests.get(url) as r:
        assert_that(r.status_code).is_equal_to(200)


def test_style():
    style_guide = flake8.get_style_guide(ignore=["E501", "W504", "ANN101", "TYP101", "TYP102"], max_line_length=140)
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    files = [os.path.join(root, "app.py")]

    errors = style_guide.check_files(files)
    assert_that(errors.total_errors).is_equal_to(0)
