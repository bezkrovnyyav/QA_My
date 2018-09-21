import unittest
from ddt import ddt, file_data
from selenium import webdriver

@ddt
class PasswordMailBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver')
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @file_data("Json_File.json")
    def test_password_validation(self, email):
        self.driver.get("https://mail.ukr.net/desktop/login")
        self.driver.find_element_by_id("id-1").send_keys("andrii_test")
        self.driver.find_element_by_id("id-2").send_keys(email)
        self.driver.find_element_by_xpath("//*[text()='Увійти']").click()

        self.assertTrue(self.driver.find_element_by_class_name("form__error form__error_fail").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()