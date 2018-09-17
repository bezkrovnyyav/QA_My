import unittest
from selenium import webdriver


class LoginMailBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver')
        self.driver.implicitly_wait(4)

    def test_my_login_in_ukr_mail(self):
        self.driver.get("https://mail.ukr.net/desktop/login")
        self.driver.find_element_by_id("id-1").send_keys("andrii_test")
        self.driver.find_element_by_id("id-2").send_keys("bezkrovnyy")
        self.driver.find_element_by_xpath("//*[text()='Увійти']").click()
        my_mail = self.driver.find_element_by_xpath("//*[@class='login-button__user']")
        assert "andrii_test@ukr.net" in my_mail.text

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
