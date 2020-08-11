from Base import utility
from Pages import Login
from Pages import caseregister


class Object:
    def __init__(self, driver):
        self.driver= driver

    def LoginPage(self):
        return Login.LoginPage(self.driver)

    def CaseRegistrationPgae(self):
        return caseregister.CaseRegistrationPage(self.driver)


