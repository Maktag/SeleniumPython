from EnvSetup.BrowserSetup import Browser
import time
from EnvSetup import BrowserSetup


class LoginTest:

    driver = None

    def start(self):
        try:
            brow = Browser()
            self.driver = brow.LaunchBrowser('firefox','https://in.yahoo.com/?p=us')
            time.sleep(2)
        except Exception as Exp:
            print("The exception is "+Exp)

    def login(self):
        try:
            self.driver.find_element_by_id('uh-signin').click()
        except Exception as e:
            print(e)


lt = LoginTest()
lt.start()
lt.login()

br = Browser()
br.CloseBrowser()