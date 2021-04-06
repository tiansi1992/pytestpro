import pytest
import yaml


class TestData:
    # def test_data(self):
    #     a=10
    #     b=20
    #     print(a+b)
    # @pytest.mark.parametrize(["a","b"], [(10, 20), (1, 2), (13, 7)])

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("./data.yaml")))
    def test_data1(self,a,b):
        print(a+b)