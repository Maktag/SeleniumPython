import webbrowser
from selenium import webdriver
import time
import os


class Browser:
    driver = None

    def LaunchBrowser(self, browserName, targetUrl):
        if browserName == 'firefox':
            self.driver = webdriver.Firefox(executable_path='/Users/ICHI01/PycharmProjects/pySel/drivers/geckodriver')
            print(os.curdir)
            print('The Firefox Browser has been launched.')
            time.sleep(5)
            self.driver.get(targetUrl)
            return self.driver
        elif browserName == 'chrome':
            self.driver = webdriver.Chrome(executable_path='/Users/ICHI01/PycharmProjects/pySel/drivers/chromedriver')
            print('The Chrome Browser has been launched.')
            time.sleep(5)
            self.driver.get(targetUrl)
            return self.driver
        elif browserName == '':
            print('No browser found.')

    def CloseCurrentTab(self):
        self.driver.close()
        print('Current Tab closed.')

    def CloseBrowser(self):
        self.driver.quit()
        print('Browser closed.')
