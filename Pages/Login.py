import configparser
from Base import utility

class LoginPage:
    def __init__(self, driver):
        self.utility= utility.utility(driver)
        self.parser = configparser.ConfigParser()
        self.parser.read(r'C:\Users\Aravind T\PycharmProjects\withframework\config\login.ini')

    def Login(self):
        self.utility.quan_navigate_url(self.parser['LOGIN']['url'])
        self.utility.quan_send_key("id", "txtUsername", self.parser['LOGIN']['username'])
        self.utility.quan_send_key("id", "txtPassword", self.parser['LOGIN']['password'])
        self.utility.quan_click("id", "btnLogin")