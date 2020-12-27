import os

import pytest
import yaml

from src.calu import Calu


@pytest.fixture(scope="module")
def beg():
    print('开始计算')
    r = Calu()
    yield r
    print('计算结束')





#
# print(os.getcwd())
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.getcwd()))
# print(os.path.join(os.path.dirname(os.getcwd()),'testdata'))
# print(os.listdir(os.path.join(os.path.dirname(os.getcwd()),'testdata')))