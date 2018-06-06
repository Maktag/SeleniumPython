from EnvSetup.BrowserSetup import Browser
import time


class LoginTest:

    driver = None

    def start(self):
        try:
            brow = Browser()
            self.driver = brow.LaunchBrowser('firefox','https://in.yahoo.com/?p=us')
            time.sleep(2)
        except Exception as Exp:
            print("The exception is "+Exp)
        return self.driver

    def login(self):
        try:
            time.sleep(3)
            self.driver.find_element_by_id('uh-signin').click()
            self.driver.find_element_by_css_selector('#login-username').send_keys('maktag28@yahoo.com')
            self.driver.find_element_by_css_selector('#login-signin').click()
            self.driver.find_element_by_css_selector('#login-passwd').send_keys('672862926589244')
            self.driver.find_element_by_css_selector('#login-signin')
        except Exception as e:
            print(e)


lt = LoginTest()

driver = lt.start()

lt.login()

Browser.CloseBrowser(driver)