from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver

driver = init_driver()


def Refresh_Page():
    driver.refresh()


def NavigateTo_Page():
    driver.


def Ecpli_wait():
    element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(By.ID,"#Id"))

def Impli_waits():
    driver.implicitly_wait(5)#in seconds

def InterActingWithEle():
    driver.find_element_by_xpath()
    driver.find_element(By.XPATH,'Xpath')
    driver.find_element_by_css_selector()
    driver.find_element_by_id()
    driver.find_element_by_class_name()
    driver.find_elements_by_class_name() # Will return all the elements

def Select_Options():
    select = Select(driver.find_elements_by_id())
    select.select_by_index()
    select.select_by_value()
    select.select_by_visible_text()
    select.deselect_by_index()
    select.deselect_by_value()
    select.deselect_by_visible_text()
    select.deselect_all()

    select.all_selected_options
    select.first_selected_option
    select.options
