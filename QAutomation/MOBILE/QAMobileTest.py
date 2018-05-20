# Libreria encargada de Test de tipo MOBILE
#               APPIUM


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.common.exceptions import TimeoutException, WebDriverException
import unittest, urllib2, socket, time, os,sys

infoTest = None

class Case(unittest.TestCase):
    PATH_PROJECT = os.path.abspath(".")
    dc = {'deviceName' : 'PhoneDevice',
          'automationName' :   'Appium',   #CAUTION: if you select UIautomator2 you will not be able to run in parallel
          'pathProject ' : PATH_PROJECT
          }
    driver = None
    port    = 4723
    host    = "127.0.0.1"

    def getInfo(self):
        info = []
        global infoTest
        for key in self.dc:
            info.append(( str(key), str(self.dc[key])   ) )
        infoTest = info
        return info

    def setUp(self):
        self.dc['clearSystemFiles'] = True

    def setClearSystemFiles(self,flag=True):
        self.first('clearSystemFiles',flag)

    def setAutomationName(self,name):
        """Wich automation engine to use.
            Appium (default) (uiautomator1)
            Selendroid
            UiAutomator2   or  Espresso for Android
            XCUITest for iOS
            YouiEngine for application built with You.i Engine"""
        self.dc['automationName'] = name

    def conf(self):
        pass

    def setOrientation(self,o):
        "(Sim/Emu-only) start in a certain orientation	LANDSCAPE or PORTRAIT"
        self.first('orientation',o)

    def setFullReset(self,fR=True):
        """Perform a complete reset
            :type Boolean
        """
        self.first('fullReset',fR)

    def setAndroidInstallPath(self,path):
        """The name of the directory on the device in which the apk will be push before install. Defaults to /data/local/tmp
        example /sdcard/Downloads/"""
        self.first('androidInstallPath',path)

    def setPlatformname(self,pfn):
        self.first('platformName',pfn)

    def setAdbPort(self,adbPort=5037):
        "Port used to connect to the ADB server (default 5037)"
        self.first('adbPort',adbPort)

    def setActivity(self,act):
        self.first('appActivity',act)

    def setPackage(self,pkg):
        self.first('appPackage',pkg)

    def setIdMobile(self,uid):
        "Funcion encargada de establecer el id unico del celular. Aqui se van a ejecutar las pruebas."
        self.uniqueID=uid
        self.first('udid',uid)

    def setPathAPK(self, pathAPK):
        self.first('app',pathAPK)

    def setNetworkSpeed(self,speed):
        "Set the network speed emulation. Specify the maximum network upload and download speeds. Defaults to full	['full','gsm', 'edge', 'hscsd', 'gprs', 'umts', 'hsdpa', 'lte', 'evdo']"

        self.first('networkSpeed',speed)

    def setBundleId_ios(self, bID):
        "Bundle ID of the app under test. Useful for starting an app on a real device or for using other caps which require the bundle ID during test startup. To run a test on a real device using the bundle ID, you may omit the 'app' capability, but you must provide 'udid'. example: io.appium.TestApp"
        self.first('bundleId',bID)

    def setGPSenabled_ios(self,flag):
        "Toggle gps location provider for emulators before starting the session. By default the emulator will have this option enabled or not according to how it has been provisioned."

        self.first('gpsEnabled',flag)

    def setLanguage(self,l='es'):
        "Sim/Emu-only) Language to set for the simulator / emulator. On Android, available only on API levels 22 and below. example: fr"

        self.first('language',l)

    def setLocationService(self,loc):
        "	(Sim-only) Force location services to be either on or off. Default is to keep current sim setting."

        self.first('locationServicesEnabled',loc)

    def setAppName_ios(self, appName ):
        "The display name of the application under test. Used to automate backgrounding the app in iOS 9+.	example UICatalog"

        self.first('appName',appName)

    def setPort(self,port):
        "systemPort used to connect to appium-uiautomator2-server, default is 8200 in general and selects one port from 8200 to 8299. When you run tests in parallel, you must adjust the port to avoid conflicts. Read Parallel Testing Setup Guide for more details. example 8201"
        self.port= port
        self.first('systemPort',port)

    def setUnicodeKeyBoard(self,k):
        "Enable Unicode input, default false"
        self.first('unicodeKeyboard',k)

    def setHost(self,host):
        self.host=host

    def setNewCommandTimeout(self, timeOut=60 ):
        "How long (in seconds) Appium will wait for a new command from the client before assuming the client quit and ending the session . DEFAUL: 60 seg"
        self.first('newCommandTimeout',timeOut)

    def first(self,key,value):
        "This function prioritizes the first data entered"
        if not(self.dc.has_key(key)):
            self.dc[key]= value

    def last(self,key,value):
        "This function override de last value"
        self.dc[key] = value

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

    def msg(self,msg):
        #FIX - Implementar que se lo agrege a los reportes - logging
        print("QAutomation: " + msg)

    def preCheck(self,verbose=False):

        if verbose:
            inf = "\n////////////////Info Test////////////////\n"
            for cap in self.dc:
                inf += cap + " :\t "+ str(self.dc[cap]) + "\n"
            inf += "////////////////////////////////////////\n"
            print inf

    def playServer(self):

        urlSERVER = 'http://'+self.host+":"+str(self.port)+'/wd/hub'
        print "Estas por entrar a - > ", urlSERVER
        try:
            self.driver = webdriver.Remote(urlSERVER, self.dc)
        except urllib2.URLError :
            print "Server Appium is not active. \nWait a moment, we will start the server..."
            AppiumServer = Server(self.host,int(self.port),"Appium Server","appium")      #Enviamos los parametros para iniciar el servidor de appium

            AppiumServer.start()                                                         #Iniciamos el servidor
            if (AppiumServer.checkServer()):                                             #Esperamos/Comprobamos que el servidor este activo
                self.driver = webdriver.Remote(urlSERVER, self.dc)  #En caso positivo nos conectamos
            else:
                print "Time exceeded to start server."
        except TimeoutException as et:
            self.driver.save_screenshot(self.PATH_PROJECT+str(et.message)+"/errorTimeOut.png")
            self.fail("Time exceeded to find a element.")
            self.tearDownClass()

        except WebDriverException:
            # print "Could not find a connected Android device. Make sure the mobile has the USB debugging option enabled"
            print "Error  WebDriver"
            self.tearDownClass()
        finally:
            return self.driver


class Server:
    """Clase encargada de gestionar el servidor
    Tener en cuenta que cada servidor debe ser par. (Ya que al crear un servidor se utiliza el siguiente para otros servicios)
    """
    WIN_PLATFORM = True if "win32" in sys.platform else False


    def __init__(self, ip='127.0.0.1',port=4723,nameServer="Appium Server",command = "Appium" ):
        self.__sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__ip   = ip
        self.__port = port
        self.__portBootsTrap = port+6
        self.__portChromeDriver = port + 4793
        self.__name = nameServer
        self.__cmd  = command


    def start(self):

        winCmd = "start cmd.exe /K "
        unixCmd = "konsole "

        if self.WIN_PLATFORM:

            cmdServer = winCmd +self.__cmd +  " -p "+str(self.__port)                                                                                                                      #+ " -bp "+str(self.__portBootsTrap) + " --chromedriver-port " + str(self.__portChromeDriver)

            os.system(cmdServer)
        else:
            cmdServer = unixCmd + self.__cmd + " -p " + str( self.__port)                                                                                                    # + " -bp "+str(self.__portBootsTrap) + " --chromedriver-port " + str(self.__portChromeDriver)

            os.system(cmdServer)
            raise NotImplementedError("Implementar funcion para otro sistema operativo")
        # os.system("start cmd.exe /K appium -p 4727 -bp 4723  --chromedriver-port 9516")

    def checkServer(self, iMax = 30):
        "Checking server port is active"

        print   "*************** Checking Server ***************"
        print "\n" , self.__name,": ",self.__ip,":",str(self.__port)#," Bootstrap port: ",self.__portBootsTrap," ChromeDriver port: ",self.__portChromeDriver,"\n"*2

        i = 0 #Intentos

        self.processServer = self.__sock.connect_ex((self.__ip, self.__port))  #Si se encuentra activo arroja 0, en caso contrario se tira un codigo de error.

        while self.processServer != 0 and  i < iMax:
            self.processServer =  self.__sock.connect_ex((self.__ip, self.__port))
            print "Server is not active. Intent : [{}/{}]".format(i,iMax)
            time.sleep(1)
            i += 1

        if (i < iMax):
            print "Server is active."
            return True
        else:
            print "Server is not active."
            return False


    def closeServer(self):
        self.processServer.close()
