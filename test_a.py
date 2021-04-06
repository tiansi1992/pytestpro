import pytest


def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[(1,2),(10,20),('a','a1')]) #参数化
def test_answer(a,b):
    assert func(a) == b

@pytest.fixture()
def login():
    print("登录操作")
    username = 'tiansi'
    return username

class TestDemo:

    def test_a(self,login):
        print(f"a username = {login}")
    def test_b(self):
        print("b")
    def test_c(self):
        print("c")

if __name__ == '__main__':
    # pytest.main(['test_a.py'])
    pytest.main(['test_a.py::TestDemo','-v'])