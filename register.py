from selenium import webdriver
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import Select
from twilio.rest import Client
from creds import user, pw, account_sid, auth_token, cell, twillio_num

class YorkRegistration:
    def __init__(self):
        
        self.client = Client(account_sid, auth_token)
        self.enrolled = False
        chromePath = r"C:\Users\jorra\Downloads\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(chromePath)
        
        
    def enrol(self, username, password):
        self.driver.get("https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem")
        try:
            sleep(2)
            self.driver.find_element_by_xpath("//input[@name=\"mli\"]").send_keys(user)
            sleep(2)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input").click()
            sleep(2)
        except: 
            print("We're already logged in.")
        try:
            sleep(2)
            Select(self.driver.find_element_by_name('5.5.1.27.1.11.0')).select_by_visible_text("Summer 2020")
            sleep(2)
            self.driver.find_element_by_name('5.5.1.27.1.13').click()
            sleep(3)
            self.driver.find_element_by_name('5.1.27.1.23').click()
            sleep(3)
            self.driver.find_element_by_name('5.1.27.7.7').send_keys('E96T01') 
            # self.driver.find_element_by_name('5.1.27.7.7').send_keys('V94K01')
            sleep(3)
            self.driver.find_element_by_name('5.1.27.7.9').click()
            sleep(3)
            self.driver.find_element_by_xpath("//input[@type=\"submit\"]").click()
            if(self.driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/span/font/b').text != 'The course has not been added.'):
                yr.enrolled = True
                message = 'We have successfully registered you in the following course: e96t01'  
                yr.message = yr.client.messages.create(body=message,
             from_=twillio_num,
             to=cell)
            else:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Deploying again in 15 Minutes. ", current_time)
                # sleep(300)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("5 Minutes have elapsed at ", current_time)
                # sleep(300)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("10 Minutes have elapsed at ", current_time)
                # sleep(300)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("15 Minutes have elapsed at ", current_time)
        except:
            print("Page has closed or is unresponsive.")
            self.driver.quit()



    def transfer(self, username, password):
        self.driver.get("https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem")
        try:
            sleep(2)
            self.driver.find_element_by_xpath("//input[@name=\"mli\"]").send_keys(user)
            sleep(2)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input").click()
            sleep(2)
        except: 
            print("We're already logged in.")
        try:
            sleep(2)
            Select(self.driver.find_element_by_name('5.5.1.27.1.11.0')).select_by_visible_text("Summer 2020")
            sleep(2)
            self.driver.find_element_by_xpath("//input[@type=\"submit\"]").click()
            sleep(2)
            self.driver.find_element_by_xpath("//input[@title=\"Transfer a Course\"]").click()
            sleep(2)
            self.driver.find_element_by_xpath("//input[@type=\"text\"]").send_keys('E96T01')
            sleep(2)
            self.driver.find_element_by_xpath("//input[@type=\"submit\"]").click()
        except:
            print("Page has closed or is unresponsive.")
            self.driver.quit()

yr = YorkRegistration() 
print("what action would you like to perform? ")
print('1. Add a course.')
print('2. Transfer a course.')
choice = 1

if(choice == 1):
    i = 0
    while not yr.enrolled and i < 50:
        i+=1
        print("Attempt #",i)
        yr.enrol(user,pw)

    if i == 50 : 
        message = 'We were unsuccessful in registering you in the following course: e96t01. Exceeded the number of attempts today, try again tomorrow.'  
        yr.message = yr.client.messages.create(body=message,from_=twillio_num,to=cell)
        yr.driver.quit()

if(choice == 2):
    i = 0
    while not yr.enrolled and i < 50:
        i+=1
        print("Attempt #",i)

        yr.transfer(user,pw)

    if i == 50 : 
        message = 'We were unsuccessful in registering you in the following course: e96t01. Exceeded the number of attempts today, try again tomorrow.'  
        yr.message = yr.client.messages.create(body=message,from_=twillio_num,to=cell)
        yr.driver.quit()