import configparser

from Base import utility

class CaseRegistrationPage:
    def __init__(self, driver):
        self.utility= utility.utility(driver)
        self.parser = configparser.ConfigParser()
        self.parser.read(r'C:\Users\Aravind T\PycharmProjects\withframework\config\login.ini')

    def Case(self):
        self.utility.quan_navigate_url(self.parser['casereg']['url'])





