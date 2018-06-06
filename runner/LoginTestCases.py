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

    @staticmethod
    def login(self):
        try:
            self.driver.find_element_by_id('uh-signin').click()
            self.driver.find_element_by_css_selector('#login-username').send_keys('')
            self.driver.find_element_by_css_selector('#login-signin').click()
            self.driver.find_element_by_css_selector('#login-passwd').send_keys('')
            self.driver.find_element_by_css_selector('#login-signin')
        except Exception as e:
            print(e)