import webbrowser
from selenium import webdriver
import time
import os


class Browser:
    driver = None

    def LaunchBrowser(self, browserName, targetUrl):
        if browserName == 'firefox':
            self.driver = webdriver.Firefox(executable_path='/Users/ICHI01/PycharmProjects/pySel/drivers/geckodriver')
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

    @staticmethod
    def CloseCurrentTab(driverPara):
        driverPara.close()
        print('Current Tab closed.')
    @staticmethod
    def CloseBrowser(driverPara):
        driverPara.quit()
        print('Browser closed.')
