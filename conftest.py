import pytest

# 测试文件不需要导入，自动寻找使用
# @pytest.fixture
# @pytest.fixture(autouse="true") # autouse导致每个用例都会执行fixture,不管有没有调用
# @pytest.fixture(scope="class") # fixture的作用域function、class、module、session
# @pytest.fixture(scope="module") # 每个文件执行一次
# @pytest.fixture(scope="session") # 多个文件只执行一次
@pytest.fixture(params=["***参数1***","***参数2***"])
def myfixture(request):
    print("执行我的fixture,里面的参数是：%s\n"%request.param)
    yield request.param # 类似于return
    print("激活fixture里面的teardown操作")

# 可以添加多个fixture
def connect_db():
    print("执行我的fixture--connect_db")
