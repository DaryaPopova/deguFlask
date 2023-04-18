import pytest


class BaseTest(pytest.TestCase):
    @pytest.fixture()
    def set_up(self):
        print('hello')
        yield
        print('goodbye')

    @pytest.fixture(scope='function')
    def some(self):
        print('begin')
        yield
        print('end')
