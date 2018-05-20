#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import  unittest #En este caso sirve unicamente para ejecutar el presente test de manera individual por consola. Es de utilidad en el caso de que necesitemos comprobar que este test no contenga errores.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import QAMobileTest


class Polizas_Test(QAMobileTest.Case):
    def conf(self):
        #Se configuran los capabilities (Se sobreescriben)
        self.setPlatformname('android')
        self.setPackage('rus.movil')
        self.setActivity('.MainActivity')
        self.setNewCommandTimeout(300)
        self.setIdMobile('TA4490EDS7')
        self.setPathAPK("C:\\Users\\Bombieri\\Desktop\\QAutomation\\MOBILE\\2018-02-19-RUSMOVIL-V1.3.1-R256-android-debug-UAT.apk")


    def setUp(self):
        "Funcion sobreescriba para ingresar datos particulares del test"
        super(self.__class__, self).setUp() #Sumamente importante para configurar las capabilities GENERALES

        self.conf()

        #Importante para comprobar que todos los datos ingresados para hacer el test esten correctos.
        self.preCheck(verbose=True)

        #Si esta todo ok, es tiempo de encargarse del servidor de Appium
        self.playServer()


    def runTest(self):
        "Funcion que ejecuta en orden las funcionalidades ingresadas. Util para hacer nuestra propia logica sobre los test."
        #Primero se va a ejecutar MisPolizas_datosOk.
        self.MisPolizas_datosOK()


    def MisPolizas_datosOK(self):
        "Funcion encargada de comprobar el flujo normal desde el inicio de la aplicacion - hasta encontrar una lista de polizas segun datos reales en la base de datos."

        self.msg( " Ejecutando -> Test Mis Polizas con datos reales" )
        #Ya que estamos ejecutando la aplicacion en modo debug (

        self.msg(" Esperando para sacar cartel de Debug")
        self.waitElement(self.driver,30,xpathElement="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button")
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button").click()

        self.msg("Esperando para sacar el cartel de inicio de completado de datos")

        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[4]/android.widget.Button")))
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[4]/android.widget.Button").click()

        self.msg("Entrando a Mis Polizas")


        self.driver.save_screenshot("prueba.png")

        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.widget.Button[2]" )))
        self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.widget.Button[2]").click()
        self.msg("Completando los datos")
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH,  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText[1]")))
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText[1]").send_keys("33992623")
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText[2]").send_keys("VAQ701")
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText[3]").send_keys("3442")
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText[4]").send_keys("1542012655")
        self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.TabWidget/android.view.View[1]/android.view.View").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText[5]")))
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.EditText[5]").send_keys("user@dominio.com")

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]").click()

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.widget.Button[2]").click()

        self.msg("Esperando a que se muestren resultados.")
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View")))







if __name__ == "__main__":
    unittest.main()