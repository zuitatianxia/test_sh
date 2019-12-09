import allure
import pytest


class TestContent:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="登录测试脚本")
    def test_login(self):
        allure.attach("输入用户名","输入用户名的描述")
        print("输入用户名")
        allure.attach("输入密码","输入密码描述")
        print("输入密码")
        allure.attach("点击登录","输入点击登录的描述")
        print("点击登录")
        assert 1

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title="用户名")
    def test_login2(self):
        print("456")
        assert 1

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step(title="密码")
    def test_login3(self):
        print("456")
        assert 1

