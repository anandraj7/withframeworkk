import unittest
from selenium import webdriver
from Base import object

class SimpleTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1280x1024")
        self.browser = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\Aravind T\PycharmProjects\withframework\Drivers\chromedriver.exe')
        self.browser.maximize_window()
        self.browser.set_page_load_timeout(25)
        self.obj= object.Object(self.browser)

    def test_Login(self):
        self.obj.LoginPage().Login()
        self.obj.CaseRegistrationPgae().Case()


    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()