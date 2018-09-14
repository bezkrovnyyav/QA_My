import unittest


from ddt import ddt, file_data
from selenium import webdriver

@ddt
class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Create a new Chrome session
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()


    @file_data("Json_File.json")
    def test_email_validation(self, email):
        self.driver.get("http://automationpractice.com")
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_name("email_create").send_keys(email)
        self.driver.find_element_by_id("SubmitCreate").click()

        self.assertTrue(self.driver.find_element_by_class_name("form-error").is_displayed())

        def tearDown(self):
            self.driver.quit()
