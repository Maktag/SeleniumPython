import unittest
from runner import LoginTest
from EnvSetup.BrowserSetup import Browser


class TestCls(unittest.TestCase):

    lt = LoginTest()
    driver = lt.start()

    def test_FirstCase(self):
        print('********************************************************************')

if __name__ == '__main__':
    unittest.main()