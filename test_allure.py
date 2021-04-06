import allure


@allure.feature("搜索模块")
class TestSearch:
    # 关联用例
    TEST_CASE_LINK='https://www.tapd.cn/48927519/sparrow/tcase/view/1148927519001010117?url_cache_key=5a7a66023aa4d013ec1b417272401e80'
    @allure.testcase(TEST_CASE_LINK,"测试用例链接")
    def test_search1(self):
        print("search1")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search2(self):
        print("search2")

@allure.feature("登录模块")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    @allure.story("登陆成功")
    @allure.title("第一个用例登录成功") #用例名称
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("登录页面")
        with allure.step("步骤3：输入用户名和密码"):
            print("输入用户名和密码")
        print("登录成功")
        pass

    @allure.story("登录失败")
    def test_login_success_a(self):
        print("登录成功")
        pass

    @allure.story("用户名缺失")
    def test_login_fail_a(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_fail_b(self):
        print("密码缺失")
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        print("登录失败")
        pass
