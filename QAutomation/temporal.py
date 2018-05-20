# #!/usr/bin/python
# # -*- coding: iso-8859-15 -*-
# import unittest
# from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
#
#
#
# class ProbandoRusMovil(unittest.TestCase):
#     "Clase de ejemplo para realizar una pequeña prueba sobre la aplicación calculadora en un celular Motorola X2 con Android 6.0"
#     dc = {}         #Inicializamos el contenedor de las capabilities - Diccionario.
#     driver = None
#
#     def setUp(self):
#         "Funcion pre-test: esta funcion se ejecuta automaticamente antes de iniciar el test."
#
#         self.dc['testName']     = 'ProbandoNombreTest'
#         self.dc['udid']         = 'TA4490EDS7'                          # Obtener este valor con el comando adb devices
#         self.dc['appPackage']   = 'com.android.calculator2'
#         self.dc['appActivity']  = 'com.android.calculator2.Calculator'
#         self.dc['platformName'] = 'android'
#         self.dc['deviceName']   = 'ERic'
#         self.dc['clearSystemFiles'] = True
#
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)
#
#
#     def testSuma(self):
#         "Funcion test: Todas las funciones iniciadas con test*, la libreria interpretara que de naturaleza para probar"
#
#         WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,
#                                                                                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Button[8]")))
#         self.driver.find_element_by_xpath(
#             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Button[8]").click()
#         self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='plus']").click()
#         self.driver.find_element_by_xpath(
#             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.Button[8]").click()
#         self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='equals']").click()
#
#     def tearDown(self):
#         "Funcion Salir: De la misma forma que setUP, esta funcion se ejecutara al finalizar el test."
#         self.driver.quit()
#
#
# #Main para probar nuestra clase
# if __name__ == '__main__':
#     unittest.main()

