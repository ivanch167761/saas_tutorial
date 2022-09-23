
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

geckodriver_loc=r"C:\nodejs\node_modules\geckodriver\geckodriver.exe"
firefox_dir=r"C:\Users\ivan.kulikov\AppData\Local\Mozilla Firefox\firefox.exe"

class BBAmpl():
    def set_browser(self, ip_address, firefox_loc, geckodrivet_loc):
        options=Options()
        self.driver = webdriver.Firefox(executable_path=geckodriver_loc, options=options)
        self.driver.get('http://%s/operatingpanel.htm'%(ip_address))



    def get_power(self):
        itemF = self.driver.find_element_by_xpath("//div[@id='justGageFwdBig0']//*[name()='svg']//*[name()='text'][2]/*[name()='tspan'][1]")
        itemR = self.driver.find_element_by_xpath("//div[@id='justGageRflBig0']//*[name()='svg']//*[name()='text'][2]/*[name()='tspan'][1]")
        return({"F":itemF.text, "R":itemR.text})

