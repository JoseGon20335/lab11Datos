import sys
import psycopg2
import utilities
import funcionesQ


def init():

    options = ["1. Estudiante", "2. Admin"]
    opcion = utilities.creaMenu(options)

    user = input("Ingrese su usuario")
    password = input("Ingrese su contraseña")

    db = psycopg2.connect(
        host="postgres",
        database="labSeguridad",
        port="5432",
        user=user,
        password=password,
        sslmode='require'
    )
    db.autocommit = True
    cursor = db.cursor()

    if(opcion == 1):
        print("Estudiante")
        estudiante(cursor, db)

    elif(opcion == 2):
        print("Administrador")
        admin(cursor, db)


def estudiante(cursor, db):
    while(True):

        options = ["1. Asignar a un curso",
                   "2. Modificación de asignación", "3. Cerrar sesión"]
        opcion = utilities.creaMenu(options)

        if (opcion == 1):
            funcionesQ.asignarse(cursor, db)

        elif (opcion == 2):
            funcionesQ.quitarasignacion(cursor, db)

        elif (opcion == 3):
            sys.exit("Adios")


def admin(cursor, db):

    while(True):

        options = ["1. Inserción de asignación", "2. Modificación de asignación",
                   "3. Eliminación de asignación", "4. Cerrar sesión de administrador"]

        selected = utilities.creaMenu(options)

        if(selected == 1):
            funcionesQ.asignacion(cursor, db)

        elif (selected == 2):
            funcionesQ.updateAsignacionAdmin(cursor, db)

        elif (selected == 3):
            funcionesQ.borrarAsignacion(cursor, db)

        elif (selected == 4):
            sys.exit("Adios")


init()
