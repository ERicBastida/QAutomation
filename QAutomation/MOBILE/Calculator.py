#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import  unittest #En este caso sirve unicamente para ejecutar el presente test de manera individual por consola. Es de utilidad en el caso de que necesitemos comprobar que este test no contenga errores.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import QAMobileTest

class ProbandoCalculator(QAMobileTest.Case):


    def conf(self,asd=None):
        if not(self.dc.has_key('udid')):
            self.setIdMobile('TA4490EDS7' )

        self.setActivity('com.android.calculator2.Calculator')
        self.setPackage('com.android.calculator2')
        # self.setPackage('com.sec.android.app.popupcalculator')
        # self.setActivity('.Calculator')
        self.setPlatformname('android')
        self.setNewCommandTimeout(120)


    def setUp(self):
        super(self.__class__, self).setUp()

        self.preCheck()
        self.playServer()

    def runTest(self):

        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Button[8]")))
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Button[8]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='plus']").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Button[8]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='equals']").click()


if __name__=="__main__":
    unittest.main()
