import unittest
from runner.LoginTestCases import LoginTest
from config.All_Variables import VarsAll


class TestCls(unittest.TestCase, VarsAll):

    def test_FirstCase(self):
        print(self._testMethodName+' is running.')
        LoginTest.login(VarsAll.driver)

    def test_SecondCase(self):
        print(self._testMethodName + ' is running.')
        LoginTest.CloseBrowser(VarsAll.driver)



if __name__ == '__main__':
    unittest.main()