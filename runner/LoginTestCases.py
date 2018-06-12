from selenium.webdriver.remote.webelement import WebElement

from EnvSetup.BrowserSetup import Browser
import time
from ReadFiles.GetData import get_data


class LoginTest:

    @staticmethod
    def login(driver):
        try:
            driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/ul/li[7]/div/button').click()
            time.sleep(5)
            for usrpass in range(len(get_data())):
                # print('UserName is: ' + get_data()[usrpass][0])
                # print('Password is: ' + get_data()[usrpass][1])
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div/form/div[1]/div/input').clear()
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div/form/div[1]/div/input').send_keys(get_data()[usrpass][0])
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div/form/div[2]/div/input').clear()
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div/form/div[2]/div/input').send_keys(get_data()[usrpass][1])
                driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div/form/div[3]/button').click()
                time.sleep(1)
                text_Msg = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/div/div/div/div/form/div[2]/div/span[2]').text
                if text_Msg == 'Invalid Email Or Password.':
                    print("For UserName "+get_data()[usrpass][0]+" & Password "+get_data()[usrpass][1]+". Test Case Passed")
                else:
                    print("For UserName " + get_data()[usrpass][0] + " & Password " + get_data()[usrpass][1] + ". Test Case Failed")
        except Exception as e:
            print(e)

    @staticmethod
    def CloseCurrentTab(driverPara):
        driverPara.close()

    @staticmethod
    def CloseBrowser(driverPara):
        driverPara.quit()