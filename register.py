from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from creds import user, pw

class YorkRegistration:
    def __init__(self, username, pw):
        chromePath = r"C:\Users\jorra\Downloads\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(chromePath)
        self.driver.get("https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"mli\"]").send_keys(user)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input").click()
        sleep(2)
        # selection_table = Select(self.driver.find_element_by_name("5.5.1.27.1.11.0"))
        # selection_table.select_by_visible_text("Summer 2020")
        sleep(2)
        # name="5.5.1.27.1.11.0"
        Select(self.driver.find_element_by_name('5.5.1.27.1.11.0')).select_by_visible_text("Summer 2020")
        sleep(2)
        self.driver.find_element_by_name('5.5.1.27.1.13').click()
        sleep(5)
        self.driver.find_element_by_name('5.1.27.1.23').click()
        sleep(5)
        self.driver.find_element_by_name('5.1.27.7.7').send_keys('E96T01') 
        sleep(3)
        self.driver.find_element_by_name('5.1.27.7.9').click()
        sleep(2)
        self.driver.find_element_by_name('5.1.27.11.9').click()

        sleep(100)

YorkRegistration(user, pw)