from DengLupage import LoginPage
from myTestCase import MyTestCase


class DengLuTest(MyTestCase):
    def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.login("test51", "123456")
