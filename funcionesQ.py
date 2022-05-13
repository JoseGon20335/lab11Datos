import utilities
import conexion

import psycopg2


def asignarse(cursor, db):
    carne = input("Ingrese su carne", 100)
    sql = ("SELECT * from curso;")
    args = ()
    results = conexion.executeQuery(cursor, db, sql, args, True)

    for item in results:
        print("\n", item[0], item[1])

    curso = input("Ingrese el ID del curso para asignarse.")

    sql = ("SELECT * from profesor;")
    values = ()
    results = conexion.executeQuery(cursor, db, sql, values, True)

    for item in results:
        print("\n", item[0], item[1], item[2])

    profesor = input(
        "Ingrese el ID del profesor que desea para este curso")

    ano = 2022

    semestre = input(
        "Ingrese el numero del semestre en el que recibirá este curso (1 o 2)", 2, 1)
    anoI = input(
        "Ingrese el numero del año en el que llevara su curso \n1. 2022 \n2. 2023")
    if(anoI == '1'):
        ano = 2022
    else:
        ano = 2023

    sql = ("SELECT count(*) from asignacion WHERE idcurso = %s and idprofesor = %s and semestre = %s and actualyear = %s;")
    values = (curso, profesor, semestre, ano)
    results = conexion.executeQuery(cursor, db, sql, values, True)

    if(results[0][0] > 30):
        print("\nYa no hay cupo en esta seccion.")
    else:
        sql = ("INSERT INTO asignaciones (idestudiante, idcurso, idprofesor, semestre, actualyear) VALUES(%s, %s, %s,%s,%s);")
        args = (carne, curso, profesor, semestre, ano)
        test = conexion.executeQuery(cursor, db, sql, args)

        if(test != False):
            print("\nSe registrado exitosamente a este curso.")


def quitarasignacion(cursor, db):

    sql = ("SELECT * from asignacion;")
    args = ()
    results = conexion.executeQuery(cursor, db, sql, args, True)

    for i in results:
        print("\n", i[5],  i[0],
              i[1], i[2], i[3], i[4])

    eliminar = input(
        "Ingrese el numero de asignacion que desea eliminar")

    sql = ("DELETE FROM asignacion WHERE idasignacion = %s;")
    args = (eliminar)
    results = conexion.executeQuery(cursor, db, sql, args)

    if(results != False):
        print("\nSe elimino la asignacion.")


def updateAsignacion(cursor, db):

    carne = input("Ingrese su carne", 100)

    sql = ("SELECT * from asignacion WHERE idestudiante = %s;")
    args = (carne,)
    results = conexion.executeQuery(cursor, db, sql, args, True)

    print('\nASIGNACIONES')
    for item in results:
        print("\n\t", item[5], "\t", item[0],
              item[1], item[2], item[3], item[4])

    updatear = input(
        "Ingrese el numero de asignacion para modificar")

    sql = ("SELECT * from profesors;")
    args = ()
    results = conexion.executeQuery(cursor, db, sql, args, True)

    for item in results:
        print("\n\t", item[0], "\t", item[1], item[2])

    profesor = input(
        "Ingrese el ID de profesor para recibir el curso")

    ano = 2022

    semestre = input(
        "Ingrese el numero del semestre en el que recibirá este curso (1 o 2)", 2, 1)
    anoI = input(
        "Ingrese el numero del año en el que llevara su curso \n1. 2022 \n2. 2023")
    if(anoI == '1'):
        ano = 2022
    else:
        ano = 2023

    sql = ("SELECT count(*) from asignaciones WHERE idprofesor = %s and semestre = %s and actualyear = %s;")
    args = (profesor, semestre, ano)
    results = conexion.executeQuery(cursor, db, sql, args, True)

    if(results[0][0] > 30):
        print("\nYa no hay cupo en esta seccion.")
    else:
        sql = ("UPDATE asignacion SET idprofesor = %s, semestre = %s, actualyear = %s WHERE idasignacion = %s and idestudiante = %s;")
        args = (profesor, semestre, ano, updatear, carne)
        test = conexion.executeQuery(cursor, db, sql, args)

        if(test != False):
            print("\nSe actualizado exitosamente este registro.")


def updateAsignacionAdmin(cursor, db):

    sql = ("SELECT * from asignacion;")
    args = ()
    results = conexion.executeQuery(cursor, db, sql, args, True)

    for item in results:
        print("\n", item[5], item[0],
              item[1], item[2], item[3], item[4])

    updatear = input(
        "Ingrese el numero de asignacion para modificar")

    sql = ("SELECT * from profesor;")
    args = ()
    results = conexion.executeQuery(cursor, db, sql, args, True)

    for item in results:
        print("\n", item[0], item[1], item[2])

    profesor = input(
        "Ingrese el ID de profesor que desea para este curso")

    ano = 2022

    semestre = input(
        "Ingrese el numero del semestre en el que recibirá este curso (1 o 2)", 2, 1)
    anoI = input(
        "Ingrese el numero del año en el que llevara su curso \n1. 2022 \n2. 2023")
    if(anoI == '1'):
        ano = 2022
    else:
        ano = 2023

    sql = ("SELECT count(*) from asignacion WHERE idprofesor = %s and semestre = %s and actualyear = %s;")
    args = (profesor, semestre, ano)
    results = conexion.executeQuery(cursor, db, sql, args, True)

    if(results[0][0] > 30):
        print("\nYa no hay cupo en esta seccion.")
    else:
        sql = ("UPDATE asignacion SET idprofesor = %s, semestre = %s, actualyear = %s WHERE idasignacion = %s;")
        args = (profesor, semestre, ano, updatear)
        test = conexion.executeQuery(cursor, db, sql, args)

        if(test != False):
            print("\nSe actualizado exitosamente este registro.")
