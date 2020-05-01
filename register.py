from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from twilio.rest import Client
from creds import user, pw, account_sid, auth_token, cell, twillio_num

class YorkRegistration:
    def __init__(self):
        self.client = Client(account_sid, auth_token)
        self.enrolled = False
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
        
        

        # sleep(100)
    def enrol(self, username, password):
        self.driver.get("https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem")
        sleep(2)
        # name="5.5.1.27.1.11.0"
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
        # print(self.driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/span/font/b').text)
        if(self.driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/span/font/b').text != 'The course has not been added.'):
            yr.enrolled = True
            message = 'We have successfully registered you in the following course: e96t01'  
            yr.message = yr.client.messages.create(body=message,
         from_=twillio_num,
         to=cell)
        else:
            print("Deploying again in 5 Minutes.")
            sleep(300)
            print("5 Minutes have elapsed")
            sleep(300)
            print("10 Minutes have elapsed")
            sleep(300)
            print("15 Minutes have elapsed")

yr = YorkRegistration()
i = 0
while not yr.enrolled and i < 50:
    i+=1
    print("Attempt #",i)
    yr.enrol(user,pw)
print(i)
if i == 50 : 
    message = 'We were unsuccessful in registering you in the following course: e96t01. Exceeded the number of attempts today, try again tomorrow.'  
    yr.message = yr.client.messages.create(body=message,
    from_=twillio_num,
    to=cell)
yr.driver.quit()