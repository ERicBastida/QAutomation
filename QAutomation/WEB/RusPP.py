# WEB/RusPP.py
# coding=utf-8

import unittest, allure, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




from QAWebTest import TestCase




pytest_plugins = 'allure.pytest_plugin',\

class Login_Test(TestCase):
    "Clase que controla el Login de RusPP"

    tURL = "http://makemake.bombieri.com.ar/rus.pp/"  #Por defecto se almacena la URL original. En caso de querer cambiarla se podra utilizar setURL


    def setUp(self):
        self.driver =super(self.__class__,self).getDriver()# webdriver.Chrome(executable_path="./Drivers/chromedriver.exe")#


        #Data base to Test in Login

        self.bd_Test =    [
            ["Fruta","Fruta", False],
            ["visbrokerprueba", "pruebaapp", True]
        ]

        self.preCheck()

    def test_first(self):

        for testData  in self.bd_Test:

            self.driver.get(self.tURL)    #"http://makemake.bombieri.com.ar/rus.pp/")
            self.verify_dataLogin(testData[0], testData[1])
            self.verify_result(testData[2])
        self.tearDown()



    @allure.step("Comprobando carga del Login")
    def verify_dataLogin(self,user=None,passw=None):
        self.driver.find_element_by_xpath("//input[@type='text']").clear()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys(user)
        self.driver.find_element_by_xpath("//input[@type='password']").clear()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(passw)
        self.driver.find_element_by_xpath("//div[3]/button").click()

    @allure.step("Comprobando las busquedas")
    def verify_result(self,Result):
        if not(Result):

            self.waitElement(self.driver,10,xpathElement="//div[2]/span")
        else:

            self.waitElement(self.driver, 10,xpathElement='//ion-toolbar/div[2]/button')



def print_classes():
    "Function return the names of classes in this module."
    current_module = sys.modules[__name__]
    names = []
    for key in dir(current_module):
        if isinstance( getattr(current_module, key), type ):
            if "Test" in key:
                names.append(key)

    return names


if __name__ == '__main__':

    unittest.main()


