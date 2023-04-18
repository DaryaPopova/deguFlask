import pytest


@pytest.fixture()
def set_up():
    print('hello')
    yield
    print('goodbye')


@pytest.fixture(scope='function')
def some():
    print('begin')
    yield
    print('end')
