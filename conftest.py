"""固定文件名 conftest.py.

存储所有的测试夹具。fixture
"""
import pytest

from config.config import WAIT_TIME
from middleware.pages.login import LoginPage
from data.login_data import login_success
from selenium.webdriver import ChromeOptions


@pytest.fixture(scope="function")
def driver():
    """管理浏览器"""

    from selenium import webdriver
    # 导入浏览器的选项类
    option = ChromeOptions()
    # 设置浏览器的可执行文件的路径
    option.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options=option)

    driver.implicitly_wait(WAIT_TIME)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    """登录"""
    user_info = login_success[0]
    LoginPage(driver).get().login_success(
        username=user_info["username"],
        password=user_info["password"])
    yield driver


