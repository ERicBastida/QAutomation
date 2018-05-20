# Libreria encargada de Test de tipo WEB
#               SELENIUM

# coding=utf-8
#!/usr/bin/python

from selenium.webdriver.support import expected_conditions
import unittest, os,sys, datetime,time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    desired_capabilities=DesiredCapabilities.CHROME)

infoTest = None

def setInfoTest(value):
    global infoTest
    infoTest = value
    sys.stderr.write("(1) Modificacion de variable " + str(datetime.datetime.now()))

def getInfoTest():
    global infoTest

    while(True):
        print "Examinando los valors"
        time.sleep(1)
        if (infoTest != None):
            return infoTest


class TestCase(unittest.TestCase):
    "Abstract Class contain principal function to define a Web test"
    #Atributos comunes a todos los test.

    dc = {  }
    port = 0
    infoTest = [("Se","Inicio")]

    tURL = ""
    driver = None
    PATH_PROJECT = (os.path.abspath(".")+"/Drivers/") if os.path.abspath(".")[-3:] == "WEB" else  (os.path.abspath(".")+"/WEB/Drivers/")
    PLATFORM = True if 'win32' == sys.platform else None


    def sysName(self):
        """
        Funcion ternaria que identifica el sistema operativo y retorna el siguiente codigo:
            True : Windows
            False: Mac
            None : Linux
        """
        sysName= sys.platform
        if 'win32' == sysName:    #Es plataforma Windows
            self.PLATFORM = True
            return "_win.exe"
        elif 'darwin' == sysName: #Manzanita
            self.PLATFORM = False
            return "_mac"
        else:
            self.PLATFORM = None
            return "_lin"            #Delmo

    def getInfo(self):
        info = []

        for key in self.dc:
            info.append(( str(key), str(self.dc[key])   ) )
        return info

    def setUp(self):
        """Esta funcion se encarga de cargar el driver para la manipulacion en el navegador.
        Hay que tener en cuenta que el driver debe estar instalado en las carpetas correspondientes
        """
        if not(self.dc.has_key('browserName')):
            nameBrowser =  ""
        else:
            nameBrowser = self.dc['browserName']

        ext = self.sysName()

        if nameBrowser == "firefox":
             self.driver = webdriver.Firefox(executable_path=self.PATH_PROJECT+"geckodriver"+ext)
        elif nameBrowser == "ie":
             self.driver = webdriver.Ie(executable_path=self.PATH_PROJECT+"IEdriver.exe")
        elif nameBrowser == "safari":
            self.driver = webdriver.Safari(executable_path=self.PATH_PROJECT+"SafariDriver.safariextz")
        else:
            self.driver = webdriver.Chrome(executable_path=self.PATH_PROJECT + "chromedriver" + ext)
        #No se han descargado
        # elif nameBrowser == "opera":
        #     driverr = webdriver.Opera()

        # elif nameBrowser == "android":
        #     driverr = webdriver.Android()
        self.preCheck()

        return self.driver

    def preCheck(self,verbose=False):

        if verbose:
            inf = "\n////////////////Info Test////////////////\n"
            for cap in self.dc:
                inf += cap + " :\t "+ str(self.dc[cap]) + "\n"
            # inf += "url : \t"+ self.tURL+"\n"
            inf += "////////////////////////////////////////\n"
            print inf



    def waitElement(self, D ,maxSeg,stepMs=500, xpathElement=None, idElement=None, tagnameElement= None,classNameElement=None,linkTextElement=None,partialLinkTextElement=None,nameElement=None,cssSelectorElement=None):

        if xpathElement != None:
            WebDriverWait(D, maxSeg ).until(expected_conditions.presence_of_element_located((By.XPATH,xpathElement)))
        if idElement != None:
            WebDriverWait(D, maxSeg ).until(expected_conditions.presence_of_element_located((By.ID,idElement)))
        if tagnameElement != None:
            WebDriverWait(D, maxSeg ).until(expected_conditions.presence_of_element_located((By.TAG_NAME,tagnameElement)))
        if classNameElement != None:
            WebDriverWait(D, maxSeg ).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,classNameElement)))
        if linkTextElement != None:
            WebDriverWait(D, maxSeg ).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,linkTextElement)))
        if partialLinkTextElement != None:
            WebDriverWait(D, maxSeg ).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT,partialLinkTextElement)))
        if nameElement != None:
            WebDriverWait(D, maxSeg ).until(expected_conditions.presence_of_element_located((By.NAME,nameElement)))
        if cssSelectorElement != None:
            WebDriverWait(D, maxSeg ).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,cssSelectorElement)))

    def tearDown(self):
        self.driver.quit()

    def setURL(self, urlTest):
        "URL to webtest page"


        self.first('url',urlTest)

    def getURL(self):
        return self.dc['url']

    def setPort(self, nport):
        """Used port when Server is running
        """
        self.port =nport
        # self.first('port',nport) #No se implementa ya que los drivers de navegadores lo hacen de forma automatica, y dejar que el usuario g

    def setBrowserName(self,nBrowser):
        """Aqui se define el nombre del Navegador Web.
        Los nombres disponibles de navegadores son :
            android, chrome, firefox, htmlunit, internet explorer, iPhone, iPad, opera, safari

        Tener en cuenta que para cada navegador existe su correspondiente driver, por lo que se tendra que descargar y almacenarlo en la carpeta Drivers.
        """

        self.last('browserName', nBrowser)

    def setBrowserVersion(self,vBrowser):
        "The browser version, or the empty string if unknown."
        self.first('version',vBrowser)

    def setPlatForm(self,pf):
        """Se define en que plataforma esta corriendo el test
            WINDOWS, XP, VISTA, MAC, LINUX, UNIX, ANDROID
        """
        self.first('platform',pf)

    def setJSenabled(self,flag=True):
        """Whether the session supports executing user supplied JavaScript in the context of the current page (only on HTMLUnitDriver).
            Type : Boolean
        """
        self.first('javascriptEnabled', flag)

    def setDataBasenabled(self, flag=True):
        """
        Whether the session can interact with database storage.
        Type : Boolean
        """
        self.first('databaseEnabled',flag)

    def setLocationContextenabled(self,flag=True):
        """
        Whether the session can set and query the browser's location context.
        Type: Boolean
        """
        self.first('locationContextEnabled',flag)

    def setApplicationCacheenabled(self,flag=True):
        """
        Whether the session can interact with the application cache.
        :type  Boolean
        """
        self.first('applicationCacheEnabled',flag)

    def setBrowserConnectionEnabled(self,flag=True):
        """
        Whether the session can query for the browser's connectivity and disable it if desired.
        :type Boolean
        """
        self.first('browserConnectionEnabled',flag)

    def setWebStorageenabled(self,flag=True):
        """
        Whether the session supports interactions with storage objects.

        """
        self.first('webStorageEnabled',flag)

    def setAccepSslCerts(self,flag=True):
        """
        Whether the session should accept all SSL certs by default.
        :type Boolean

        """
        self.first('acceptSslCerts',flag)

    def setRotatable(self, flag=True):
        """
        Whether the session can rotate the current page's current layout between portrait and landscape orientations (only applies to mobile platforms).
        :type Boolean

        """
        self.first('rotatable',flag)

    def setNativeEvents(self, flag=True):
        """
        Whether the session is capable of generating native events when simulating user input.
        :type Boolean

        """
        self.first('nativeEvents',flag)

    def setProxy(self, proxy_object=None):
        """
        Details of any proxy to use. If no proxy is specified, whatever the system's current or default state is used. The format is specified under Proxy JSON Object.
        :type Proxy object

        """
        self.first('proxy',proxy_object)

    def setUnexpectedAlertBehaviour(self, action="ignore"):
        """
        What the browser should do with an unhandled alert before throwing out the UnhandledAlertException. Possible values are "accept", "dismiss" and "ignore"
        :type String

        """
        self.first('unexpectedAlertBehaviour',action)

    def setElementScrollBehavior(self, behavior="ignore"):
        """
         Allows the user to specify whether elements are scrolled into the viewport for interaction to align with the top (0) or bottom (1) of the viewport. The default value is to align with the top of the viewport. Supported in IE and Firefox (since 2.36)
        :type Integer

        """
        self.first('elementScrollBehavior',behavior)

    def first(self,key,value):
        "This function prioritizes the first data entered"

        if not(self.dc.has_key(key)):
            self.dc[key]= value

    def last(self,key,value):
        "This function override de last value"
        self.dc[key] = value











