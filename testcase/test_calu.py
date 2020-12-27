import pytest

from src.calu import Calu
from src.readdata import read_data


class Test_claul():



    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,excepted",read_data('../testdata/adddata.yml')['Add'],ids=read_data('../testdata/adddata.yml')['idsname'])
    @pytest.mark.usefixtures('beg')
    def test_add(self,beg,a,b,excepted):
        assert beg.add(a,b) == excepted

    @pytest.mark.parametrize("a,b,excepted", read_data('../testdata/divdata.yml')['Div'],
                             ids=read_data('../testdata/divdata.yml')['idsname'])
    def test_div(self, beg,a, b, excepted):
        assert beg.div(a, b) == excepted

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,excepted",read_data('../testdata/subdata.yaml')['Sub'],ids=read_data('../testdata/subdata.yaml')['idsname'])
    def test_sub(self,beg,a,b,excepted):
        assert beg.sub(a,b) == excepted
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,excepted", read_data('../testdata/muldata.yml')['Mul'],ids=read_data('../testdata/muldata.yml')['idsname'])
    def test_mul(self,beg,a,b,excepted):
        try:
            result = beg.mul(a,b)
            if isinstance(result,float):
                result = round(result,2)
        except Exception as e:
            print(e)
        assert result == excepted


