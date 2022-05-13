# import re
# import hashlib
# from datetime import datetime


def creaMenu(opciones):
    print("Ingrese una de las siguientes opciones:\n")
    menu = ""
    for i in opciones:
        menu = menu + i + "\n"

    while(True):
        userData = input(menu)
        try:
            inputData = int(userData)

            if inputData <= len(opciones):
                return(inputData)
            else:
                print("Ingrese una opción válida")
        except:
            print("La opcion debe ser un numero")
