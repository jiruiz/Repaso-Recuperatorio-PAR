import csv
import os

def pedirNombre():
    while True:
        nombre = input("Se creará un archivo \n\tingrese nombre del archivo que desea crear:  ")
        try:
            return str(f"{nombre}.csv")
        except ValueError:
            print("error al nombrar archivo")

def pedirArchivo():
    while True:
        nombre = input("\tingrese nombre del archivo que desea recuperar:  ")
        try:
            return str(f"{nombre}.csv")
        except ValueError:
            print("error al nombrar archivo")


def cargardatos(archivo,campos):
    guardar = "si"
    filasCarga = []
    while guardar == "si":
        empleado = {}

        for campo in campos:
            empleado[campo] = input(f"Ingrese {campo} del Empleado: ")
        filasCarga.append(empleado)
        guardar = input("Desea seguir agregando empleados? Si/No")

    try:
        nombreArchivo = pedirNombre()
        hayAlgunArchivo = os.path.isfile(archivo)

        with open(archivo, 'a', newline='') as file:
            archivoAGrabar = csv.DictWriter(file, fieldnames=campos)

            if not hayAlgunArchivo:
                archivoAGrabar.writeheader()

            archivoAGrabar.writerows(filasCarga)
            print("Empleado Cargado Exitosamente!")
            return
    except IOError:
        print("no se reconoce el archivo.")


def recupero(archivo):

   archivo2 = pedirArchivo()
   try:#intentar
       with open(archivo, 'r', newline='') as file:
         with open(archivo2, "r", newline='') as file2:
           fileCSV = csv.reader(file, delimiter=";")
           file2CSV = csv.reader(file2)

           itemEmpleados = next(file2, None)
           itemLegajos = next(file, None)
           busqueda = input("legajo a buscar: ")

           contador = 0
           diasAdeudados = 0
           diasTotalesDeVacaciones = 0
           numeroLegajo = 0
           for linea in fileCSV:#POR CADA LINEA EN EL ARCHIVO DE LEGAJOS, ENTONCES

             if busqueda in linea[0]:# SE HACE LA BUSQUEDA EN LA POSICION 0 DE LA LINEA, SI ESTO SE DA,

                 contador += 1# SE SUMA UNO AL CONTADOR DE CADA DIA

                 for vuelta in file2CSV:#PARA CADA VUELTA(LINEA) EN EL ARCHIVO DE EMPLEADOS,

                   numeroLegajo = int(vuelta[0])#LA POSICION 0 DE ESA LINEA, SE ALMACENA EN LA VARIABLE NUMEROlEGAJOS
                   diasTotalesDeVacaciones = int(vuelta[3])#LOS DIAS TOTALES DE

                   if busqueda in vuelta[0]:

                     diasAdeudados = diasTotalesDeVacaciones - contador
                     print(f"Legajo N°: {numeroLegajo}:  {vuelta[1]}")

       print(f'\tse tomó: {contador} dias, debe {diasAdeudados}')
       #print(f"el consumo total general es de {totalGeneral}")
   except IOError:
       print("Hubo un error al abrir el archivo.")
   except ValueError:
       print("debe ingresar un entero")













def main():

    LEGAJOS= "legajo.csv"
    CAMPOS = ['Legajo','Apellido','Nombre','Total Vacaciones']
    CAMPOSLEGAJOS = ['Legajo','Fecha']
    while True:
        print("\tElija una opcion:\n\t 1.Cargar datos de Empleados \n\t 2.Consulta dias de VacacionesPendientes\n\t 3.Salir")
        opcion = input("")


        if opcion == "1":

            archivo = pedirNombre()
            cargardatos(archivo, CAMPOS)


        if opcion == "2":
            archivo = input("ingrese nombre del archivo a recuperar")
            try:
                recupero(f"{archivo}.csv")
            except IOError:
                print("error de lectura I/O")
            # except:
            #     print("otro tipo de error")

        if opcion == "3":
            exit()
        else:
            print("elija una opcion valida")
main()
