import pytest


class TestMark():
    @pytest.mark.smoke
    def test_one(self):
        print("我的第一个用例")
    @pytest.mark.demo
    def test_two(self):
        print("我的第二个用例")
