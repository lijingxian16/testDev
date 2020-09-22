from selenium.webdriver.common.by import By
from web.ob.base_page import BasePage


class Register(BasePage):
    def scan(self):
        pass

    def goto_register(self):
        self.find(By.CSS_SELECTOR, "login_registerBar_link").click()
        return Register(self._driver)


if __name__ == "__main__":
    pass
