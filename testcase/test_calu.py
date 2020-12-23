import pytest

from src.calu import Calu
from src.readdata import read_data


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
    @pytest.mark.parametrize("a,b,excepted",read_data('../testdata/adddata.yml')['Add'],ids=read_data('../testdata/adddata.yml')['idsname'])
    def test_add(self,a,b,excepted):
        assert self.calu.add(a,b) == excepted

    @pytest.mark.parametrize("a,b,excepted",read_data('../testdata/subdata.yaml')['Sub'],ids=read_data('../testdata/subdata.yaml')['idsname'])
    def test_sub(self,a,b,excepted):
        assert self.calu.sub(a,b) == excepted

    @pytest.mark.parametrize("a,b,excepted", read_data('../testdata/muldata.yml')['Mul'],ids=read_data('../testdata/muldata.yml')['idsname'])
    def test_mul(self,a,b,excepted):
        assert self.calu.mul(a,b) == excepted

    @pytest.mark.parametrize("a,b,excepted", read_data('../testdata/divdata.yml')['Div'],ids=read_data('../testdata/divdata.yml')['idsname'])
    def test_div(self,a,b,excepted):
        assert self.calu.div(a,b) == excepted
