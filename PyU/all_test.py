import unittest
from runner.LoginTestCases import LoginTest
from config.All_Variables import VarsAll

class TestCls(unittest.TestCase, VarsAll):

    # lt = LoginTest()
    # driver = lt.start()
    # driver = LoginTest.driver

    def test_FirstCase(self):
        print(self._testMethodName+' is running.')
        self.lt.login()

    def test_SecondCase(self):
        print(self._testMethodName + ' is running.')
        self.lt.CloseBrowser(self.driver)


if __name__ == '__main__':
    unittest.main()