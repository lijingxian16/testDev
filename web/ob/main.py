from web.ob.base_page import BasePage
from selenium.webdriver.common.by import By
from web.ob.login import Login
from web.ob.login import Register


class Main(BasePage):
    _base_url = "http://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)



if __name__ == "__main__":
    # pytest testcase --alluredir report/allure_raw
    pass
