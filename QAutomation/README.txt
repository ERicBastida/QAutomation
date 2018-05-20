 - QA Automation -
                    //Esta herramienta esta encargada de ejecutar los Test pertinentes a las aplicaciones, ya sean, Web o Mobile.
                    //Una vez finalizado los test nos mostrara los reportes generados en formato HTML.

                    USO DIRECTO:
                                        WEB/MOBILE     PACKAGE.TEST.FUNCTION             PATH_REPORT
                    python QAutomation    -[W/M]     NameFile.TestClass.TestFunc      -r  ./NAME_FOLDER/

                    NameFile: Tener en cuenta que el nombre del paquete debe ser el mismo que el nombre del archivo. Por lo que se debera buscar en la carpeta WEB o APP el nombre de archivo a ejecutar.
                    TestClass: Dentro del archivo perteneciente a la aplicacion, podemos seleccionar que prueba deseeamos ejecutar.
                    TestFunc: Nombre de la funcionalidad dentro de una clase que deseeamos iniciar.

                    En caso, de unicamente ejecutar un nivel mas general, ingresamos el nombre del paquete.


                    Tomando como ejemplo la siguiente estructura de una aplicacion movil llamada Calculadora:

                    Calculadora.py
                        |_Botones_Test
                        |     |_Tocar_boton_1
                        |     |_Tocar_boton_n
                        |_Resultado_Test
                        |     |_Suma
                        |     |_Resta
                        |_Guardar_Test
                              |_guardar_log

                    python QAutomation -m Calculadora.Botones_Test Calculadora.Guardar_Test



Tener en cuenta que cada vez que generamos un test debemos:
    Si es de tipo WEB agregar lo/s metodo/s

            setURL   (Que sobreescriba la URL ya ingresada.)

    Si es de tipo MOBILE agregar lo/s metodo/s

            setUID  (Para hacer pruebas paralelizadas)

