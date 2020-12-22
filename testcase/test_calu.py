import pytest

from src.calu import Calu


class Test_claul():
    def setup_class(self):
        self.calu = Calu()
        print('开始测试')


    def teardown_class(self):
        print('结束测试')

    def setup(self):
        print('开始计算')

    def teardown(self):
        print('结束计算')
    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b,excepted",[(2,2,4)])
    def test_add(self,a,b,excepted):
        assert self.calu.add(a,b) == excepted
