from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest:

    def setup_method(self, method):
        # 声明一个变量，设置为chrometoptions
        chrome_opts = webdriver.ChromeOptions()
        # set address same as chrome debugging port
        chrome_opts.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_opts)

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        sleep(3)
        # self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
