# coding=utf-8
#!/usr/bin/python

__author__ = 'ERic Bastida'
__name__   = 'QA Automation'
__version__ = '0.8'



import   importlib, unittest,  os ,sys, datetime,shutil,webbrowser




#import HtmlTestRunner Libreria original
import lib.htmlTestrunner.HTMLTestRunner as Runner #Libreria modificada


class ManagerQA():
    "Clase encargada de gestionar todos los test confeccionados, ya sean Web o Moviles."



    PATH_PROJECT       = os.path.abspath(".")
    PATH_WEB           = os.path.abspath("./WEB")
    PATH_WEB_REPORT    = os.path.abspath("./WEB/REPORTS")
    PATH_WEB_DRIVERs   = os.path.abspath("./WEB/Drivers")
    PATH_MOBILE        = os.path.abspath("./MOBILE")
    PATH_MOBILE_REPORT = os.path.abspath("./MOBILE/REPORTS")

    WEB_FOLDER        = "WEB"                            #Nombre de la carpeta dentro del proyecto donde se buscaran los test de tipo WEB (Selenium)
    MOBILE_FOLDER     = "MOBILE"                         #Nombre de la carpeta dentro del proyecto donde se buscaran los test de tipo Mobile (Appium)

    WEB_test = True                                      #Los test se realizan en la parte WEB, sirve para ubicar los test en su correspondiente carpeta
    test = None
    SHOW_REPORT = True


    WIN_PLATFORM = True if "win32" in sys.platform else False
    infoProject = [
        ('QAutomation ','2018'),
        ('Company ', 'BOMBIERI'),
        ('Version', __version__),
    ]

    infoTest = [
        ('Name Test ', 'Example'),
        ('Type', 'WEB/MOBILE')
    ]

    def __init__(self, argv):
         """Funcion inicial al momento de correr la aplicacion.
         Se va a encargar de:
            Mostrar informacion de uso. (Sin enviar parametros)
            Mostrar nombre de los test guardados en las carpetas de proyectos WEB's y Mobile.
            Validar los datos ingrsados
            Ejecutar los test pertinentes
            Generar los reportes de cada test.

        """




         if argv.__len__() == 0:   #Modo info, sin argumentos

             print """ - QA Automation -
                         //Esta herramienta esta encargada de ejecutar los Test pertinentes a las aplicaciones, ya sean, Web o Mobile.
                         //Una vez finalizado los test nos mostrara los reportes generados en formato HTML.

                         USO DIRECTO:
                                             WEB/MOBILE     PACKAGE.TEST.FUNCTION        PARAMETERS                 (r)EPORT (path)       PORT_IF_NECESARY (to parallel test)
                                QAutomation    -[w/m]          nameFileTest.py      [options / dataOption]     --rpath  ./NAME_FOLDER/         --port NUMBER_PORT


                        [options] WEB:
                                                        FOR EXAMPLE
                              -u    URL_WEB_TEST        https://www.google.com.ar/
                              -b    NAME_BROWSER        android, chrome, firefox, htmlunit, internet explorer, iPhone, iPad, opera, safari
                              -bv   VERSION_BROWSER     54.0

                        [options] MOBILE:
                                                        FOR EXAMPLE
                              -p   pathAPK                C:/APKs/appToTest.apk
                              -d   uniqueDeviceID         TASD15315
                              -pkg package                com.android.calculator2'
                              -act activity               .MainActivity


                         BUSQUEDA DE PROYECTOS DISPONIBLES:

                                 QAutomation -[pw/pm]

                                 pw: Proyectos Webs diponibles
                                 pa: Proyectos Moviles disponibles

                        """
             # sys.stdout.flush()

         else: #En caso de tener algun tipo de argumento...

            #Diccionario que contiene los parametros para ejecutar el test.


            projectsAPP = "-pw" in argv
            projectsWEB = "-pm" in argv

            if projectsAPP or projectsWEB:  #Pregunto si tengo algun paramatro que indique mostrar informacion de proyectos.

                if projectsAPP:
                    print self.showProjects(web=True).values()
                else:
                    print self.showProjects(web=False).values()
            else:  #En caso de ser un comando comun

                #Argumentos a pasar al ejecutor del Test (ya validados)
                self.argsQA = {
                    'web': False,  # Para saber que tipo de parametros debo sacar.
                    'url': "",
                    'app': "",
                    'appPackage': "",
                    'appActivity': "",
                    'udid': "",
                    'nameTest': "",

                    'pReportes': "",
                    'port': "",
                    'browser' : "",
                    'browserVersion':""

                }

                self.argv = argv

                if "-w" in argv[0].lower(): #Si el primer parametro tiene una w, quiere decir que es WEB
                    self.argsQA['web'] = True       #Comprueba si es de tipo WEB para buscar en la correspondiente carpeta.
                    self.__getArg("-w",'nameTest')
                    self.__getArg("-u",'url')       #Si es un test tipo web va a necesitar la URL donde se va a realizar el test.
                    self.__getArg("-b",'browser')
                    self.__getArg("-bv",'browserVersion')

                elif "-m" in argv[0].lower():

                    self.__getArg("-m",'nameTest')  # Si es un test tipo web va a necesitar la URL donde se va a realizar el test.
                    self.__getArg("-p",'app')       #Consultando el caso de tener el path de la APK.
                    self.__getArg("-d",'udid')      #Consulta de la existencia del ID del Device
                    self.__getArg("-pkg",'appPackage')      #Consulta de la existencia del ID del Device
                    self.__getArg("-act",'appActivity')      #Consulta de la existencia del ID del Device

                else:
                    print "QAutomation - INVALID ARGUMENTS  - Please input type of your proyect [-w (web) / -m (mobile) ]"
                    sys.exit(2)
                self.__getArg("--port", 'port')  # Con objetivos de paralelizacion, en caso de no enviarlo quiere decir que se va a ejecutar un solo test.
                self.__getArg("--rpath",'pReportes')


                self.play(self.argsQA)

    def __getArg(self,arg,key):
        "Funcion encargada de preguntar por la existencia de un parametro-valor en los argumentos enviados por consola"
        if (arg in self.argv):
            if (self.argv[self.argv.index(arg) + 1] != ""):  # Si es un test tipo web va a necesitar la URL donde se va a realizar el test.
                self.argsQA[key]=  self.argv[self.argv.index(arg) + 1]

    def play(self, argsQA, showReport=False):
        """Funcion que ejecuta las pruebas y muestra los reportes
        wa : True = WEB   False=APP
        cmd: Modulos Modulo.Test Modulo.Test.Func. Separador por espacio
        pathHTML: Ruta relativo o Absoluta donde se guardaran los reportes. En caso de recibir vacio, se almacenaran en la carpeta ReportesHTML dentro del proyecto.
        showReport= Ejecuta un servidor web para mostrar los reportes. Caso contrario solamente se los almacenará.
        """

        if argsQA['web']:
            self.WEB_test = True
            Type = self.WEB_FOLDER                #Nombre de la carpeta donde se encuentran los test de proyectos WEB

        else:
            Type = self.MOBILE_FOLDER            #Nombre de la carpeta donde se encuentran los test de proyectos WEB
            self.WEB_test = False


        loader = unittest.TestLoader()


        print " - - - ", Type, " - - - ", argsQA['nameTest']

        self.SUITES = self.getClassTest(loader.discover(Type, pattern=argsQA['nameTest']))


        if self.SUITES == None: #Ya las mismas funciones internamenta terminan la aplicacion en caso de no encontrrar test,pero por las dudas.
            sys.exit(2)


        # FIX - AGREGAR LAS OPCIONES AQUI
        if argsQA['pReportes'] == "":
            if self.WEB_test:
                argsQA['pReportes'] = self.PATH_WEB_REPORT
            else:
                argsQA['pReportes'] = self.PATH_MOBILE_REPORT
        else:
            shutil.copytree('lib/htmlTestrunner/srcReport/', argsQA['pReportes'])




        if argsQA['web']:

            if argsQA['url'] != "":
                self.setParameters("setURL",argsQA['url'])
            if argsQA['browser'] != "":
                self.setParameters("setBrowserName", argsQA['browser'])
            if argsQA['browserVersion'] != "":
                self.setParameters("setBrowserVersion", argsQA['browserVersion'])
            if argsQA['port'] != "":
                self.setParameters("setPort", argsQA['port'])




        else: #En caso de ser un proyecto de tipo mobile
            if argsQA['app'] != "":
                self.setParameters( "setPathAPK", argsQA['app'])
            if argsQA['udid'] != "":
                self.setParameters("setIdMobile", argsQA['udid'])

            if argsQA['appPackage'] != "":
                self.setParameters("setPackage", argsQA['appPackage'])

            if argsQA['appActivity'] != "":
                self.setParameters( "setActivity", argsQA['appActivity'])

            if argsQA['port'] != "":
                self.setParameters( "setPort", int(argsQA['port']))


        #Con esta funcion se obtiene la informacion de cada test, para mostrarlo en el reporte
        self.setParameters("conf", None)

        print "\n//////////////////////////////////////////////"
        print "|               QAutomation                  |"
        print "//////////////////////////////////////////////"
        # sys.stdout.flush()
        # print "\n["+Type+"]Nombre/s de Test/s : " + argsQA['nameTest']
        
        print     "     -------- INICIANDO PRUEBAS   -------- "
        # sys.stdout.flush()
        #Arming Suites...
        self.arm()

        nameFile="QAtest-"+argsQA['nameTest'][:-3]+datetime.datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')+".html"

        pathFile = argsQA['pReportes']+"/"+nameFile
        fp = open(pathFile,"w+")

        RUN = Runner.HTMLTestRunner(verbosity=1,stream=fp ,title="QAutomation - "+argsQA['nameTest'][:-3],attrs=self.make_attrs(),description="")
        RUN.run(self.SUITES)

        # HtmlTestRunner.HTMLTestRunner(verbosity=2,output=argsQA['pReportes'],report_title="QAutomation - "+argsQA['nameTest'][:-3]).run(SUITEQA) #Con la libreria original


        print "\n\n      -------- PRUEBAS FINALIZADAS -------- \n\n"
        # sys.stdout.flush()
        print "Generating HTML report..."
        print pathFile  # ,"\n","Opening..."

        if self.SHOW_REPORT :
            print "\nOpening..."
            import webbrowser
            webbrowser.open_new_tab(pathFile)

    def arm(self):
        "Funcion encargada de traducir todos los test(clases crudas) encontrados en un formato aceptable para unittest"

        Suites = []
        for suite in self.SUITES:
            S = unittest.TestSuite()
            for test in suite:
                S.addTest(test)
                # self.infoTest = test.getInfo()
                # print "INFO TEST", self.infoTest
                # self.t =test #Guardo un test para luego de ser ejecutado que me almacene la info
            Suites.append(S)

        # masterSuite

        self.SUITES = unittest.TestSuite(Suites)

    def setParameters(self,func,args):
        for suite in self.SUITES:
            for test in suite:
                if func == "conf":
                    test.conf()
                    self.infoTest = test.getInfo()
                    print test.getInfo() , test.__str__()
                # print "test> Test."+func,"(",str(args),")"
                if args == None:
                    test.__getattribute__(func)()
                else:
                    test.__getattribute__(func)(args)

    def make_attrs(self,infoTest=None):
        if infoTest != None:
            self.infoTest = infoTest
        attrs = {'group2': self.infoTest, 'group3': self.infoProject}
        return attrs

    def setPathReportsJSON(self, path):
         """Cambia el directorio donde se almacena los reportes en formato JSON
         path = ./Path_do_you_want/d
         Recordar que el punto indica que el PATH se establece de forma relativa a la posicion actual del proyecto.
         De esta menera descartamos la sintaxis de los directorios dependientes del sistema operativo.
         """
         # self.PATH_semiReportes = path

    def setPathReportsHTML(self, path ):
        """Cambia el directorio donde se almacena los reportes en formato HTML
        path = ./Path_do_you_want/ o C:/Reports
        Recordar que el punto indica que el PATH se establece de forma relativa a la posicion actual del proyecto.
        De esta menera descartamos la sintaxis de los directorios dependientes del sistema operativo.

        """
        # if os.path.isdir(path): check if path is correct
        # self.PATH_semiReportes = path

    def showProjects(self, web=True):
        """Muestra en un diccionario en pantalla los Modulos de Tests disponibles en el directorio.
         Web = True   : Nos mostrara los Test disponibles para los proyectos WEBs. Es decir, buscara en la carpeta WEB.
         Web = False  : Nos mostrara los Test disponibles para los proyectos Moviles. Busca en la carpeta APP
        """
        r = dict()

        ProjecType = str((self.WEB_FOLDER) * web) + str((self.MOBILE_FOLDER) * (not web))
        print "\t* * * PROYECTOS " + ProjecType + "'s DISPONIBLES * * *"

        if "win32" in sys.platform:

            currentDir = os.popen("cd",'r').read()

            cmdWin1 = "cd " + currentDir[:-1]+"\\"+ ProjecType
            cmdWin2 = "dir *py /B"
            result = os.popen(cmdWin1+" && "+cmdWin2,'r').read()
            result = result.split("\n")


        else:
            currentDir = os.popen("pwd",'r').read()
            cmdUnix1 = "cd " + currentDir[:-1]+ "\\"+ProjecType
            cmdUnix2 = "ls *.py "

            result = os.popen(cmdUnix1+" && "+cmdUnix2,'r',).read()
            result = result.split("\n")

        for i in range(result.__len__()):
            if result[i] != '' and result[i] != "__init__.py" and result[i] != "Server.py" and result[i] != "QAWebTest.py" and result[i] != "QAMobileTest.py":  # Filtro para no mostrar archivos del sistema
                r[i] = result[i]

        return r

    def listTestofModule(self,moduleName):
         "Según un modulo en especifico muestra los Test que se pueden realizar "

         moduleName= moduleName[:-3]                 #Quito la extensión del archivo para importarlo
         if self.WEB_test:
             moduleName = self.WEB_FOLDER+"."+ moduleName
         else:
            moduleName = self.MOBILE_FOLDER+"."+ moduleName

            modulo = importlib.import_module(moduleName)

         return modulo.print_classes()

    def getClasses(self,list):

        if list.countTestCases() == 0:
            print "QAutomation - We didn't find any Test."
            sys.exit(0)

        l = []
        for test in list:

            if str(type(test)).__contains__("TestSuite"):
                l2 = self.getClasses(test)
                if l2.__len__() > 0:
                    l.append(l2)
            elif "Failure" in str(type(
                    test)):  # Este if se debe a que puede encontrar el test correspondiente, pero el mismo contiene errores.
                print "QAutomation - Error to load test. Make sure your test is correct."
                sys.exit(1)
            else:
                l.append(test)
                # print test.__str__(), type(test)
        return l

    def normalize(self, lista):

        if isinstance(lista[0][0], list.__class__):
            self.normalize(lista[0])
        else:
            return lista[0]

    def getClassTest(self, list):
        "De una lista cruda que nos brinda Unittest-Discovery se retorna un una lista ordenada los test (clases) encontrados, con el fin de asignarle los atributos correspoondientes."
        print "----Clases encontradas----"
        print list.__str__()
        listTest = self.getClasses(list)  # Se obtienen de los suites, todos los test individuales
        normListTest = self.normalize(listTest)  # Para no tener lista dentro de otras listas (y asi sucesivamente, por recursividad). Esta funcion envia en una lista, un conjunto de listas que pertenecen a cada SUITE. Es decir una lista de SUITES

        return normListTest

if __name__ == 'QA Automation':

    #------------- Pruebas por consola -------------

    Mng = ManagerQA(sys.argv[1:])  # sys.argv son los parametros que se envian por consola

    # ------------- Pruebas por Pycharm ------------
    #                    DEBUGGING

    # ManagerQA(["-w","Youtube.py", "-b","chrome"])






