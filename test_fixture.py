
import pytest

# 提取到conftest.py文件
# @pytest.fixture()
# def myfixture():
#     print("执行我的fixture")

class TestDemo():
    def test_one(self):
        print("执行test_one")
        assert 1+1==2

    def test_two(self):
        print("执行test_two")
        assert 1+1==2

    def test_three(self):
        print("执行test_three")
        assert 1+1==2

