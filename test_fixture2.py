import pytest


class TestDemo2():
    def test_one2(self,myfixture):
        print("执行test_one2")
        assert 1+1==2

    def test_two2(self,myfixture):
        print("执行test_two2")
        assert 1+1==2

    @pytest.mark.flaky(reruns=2,reruns_delay=3)
    def test_three2(self):
        print("执行test_three2")
        assert 1 ==2


    def test_four2(self):
        print("执行test_four2")
        pytest.assume(1==2)
        pytest.assume(1==3)
        pytest.assume(1==1)