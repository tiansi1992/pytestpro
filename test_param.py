import pytest
import yaml


def add_function(a,b):
    return a+b

# @pytest.mark.parametrize(
#     "a,b,expected",
#     [(1,2,3),(-1,-1,-3),(10000,10001,20000)],
#     ids=['int','minus','bigint']
# ) #ids 给各组用例添加别名，增加阅读性

# @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open("./data2.yaml"))["datas"],
#                          ids=yaml.safe_load(open("./data2.yaml"))["myid"])

# 封装
def getdatas():
    with open("./data2.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myid"]
        return[add_datas,add_ids]
@pytest.mark.parametrize("a,b,expected",getdatas()[0],ids = getdatas()[1])
def test_add(a,b,expected):
    assert add_function(a,b)==expected



#测试数据排列组合
# @pytest.mark.parametrize("a",[0,1])
# @pytest.mark.parametrize("b",[2,3])
# def test_add(a,b):
#     print("测试数据组合：a->%s,b->%s"%(a,b))