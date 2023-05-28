import os
import re
import json


'''
BIBLIOTECAS
- Main (Cargar la lista del json y llamar la función del Menu)
- Menu
- Funciones
- Archivos

'''


estadisticas_palabras_validar = r'[temporadas|puntos_totales|promedio_puntos_por_partido|rebotes_totales|promedio_rebotes_por_partido|asistencias_totales|promedio_asistencias_por_partido|robos_totales|bloqueos_totales|porcentaje_tiros_de_campo|porcentaje_tiros_libres|porcentaje_tiros_triples]'
path = "C:/Users/dcris/Desktop/UTN/Laboratorio2023/Ejercicios/Ejercicios/data_dream_team.json"

def clear_console() -> None:
    """
    It waits for the user to hit enter
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('\nPresione cualquier tecla para continuar...')
    os.system('cls')

def leer_archivo (nombre_archivo:str) -> list:
    '''
    Recibe el nombre del archivo a abrir (o el path)
    Crea una lista y abre el archivo que le pasamos en formato de lectura. A la lista asigna el dato dict
    Retorna la lista con los datos del archivo json
    '''
    lista_jugadores = []
    with open (nombre_archivo, "r") as archivo: #Abrir el archivo (Para abrirlo no hace falta especificarle el "r", por default se abre en modo lectura)
        dict = json.load(archivo) #Procesarlo
        lista_jugadores = dict["jugadores"]
    return lista_jugadores

def mostrar_jugador_nombre_posicion(jugador:dict):
    '''
    Recibe un jugador.
    Chequea si el dict del jugador esta vacío.
    Printea con el formato Nombre xxx - yyy(posicion)
    '''
    if jugador is not None:
        print("Nombre: {0} - {1}".format(jugador["nombre"],jugador["posicion"]))

def mostrar_jugador_nombre_dato(jugador:dict,dato:str):
    '''
    Recibe un jugador.
    Chequea si el dict del jugador esta vacío.
    Printea con el formato Nombre xxx - yyy(posicion)
    '''
    if jugador is not None:
        print("Nombre: {0} \t- {1}: {2}".format(jugador["nombre"],dato,obtener_dato(jugador,dato)))

def mostrar_lista_jugadores_nombre_dato (lista:list,dato:str):
    '''
    Recibe una lista y confirma que no este vacía
    La recorre e imprime por consola los jugadores y su posicion
    En caso de que la lista este vacía muestra un mensaje de error 
    '''
    if len(lista) > 0:
        for jugador in lista:
            mostrar_jugador_nombre_dato(jugador,dato)
    else:
        print("Lista sin elementos para imprimir")

def mostrar_lista_jugadores_nombre_posicion (lista:list):
    '''
    Recibe una lista y confirma que no este vacía
    La recorre e imprime por consola los jugadores y su posicion
    En caso de que la lista este vacía muestra un mensaje de error 
    '''
    if len(lista) > 0:
        for jugador in lista:
            mostrar_jugador_nombre_posicion(jugador)
    else:
        print("Lista sin elementos para imprimir")       

def mostrar_lista_jugadores_indice (lista:list):
    '''
    Recibe una lista y confirma que no este vacía
    La recorre e imprime por consola los jugadores y un índice
    En caso de que la lista este vacía muestra un mensaje de error 
    '''
    if len(lista) > 0:
        indice = 1
        for jugador in lista:
            print("{0}. {1}".format(indice,jugador["nombre"]))
            indice += 1
    else:
        print("Lista sin elementos para imprimir")

def mostrar_estadisticas_jugador(jugador:dict):
    '''
    Recibe un jugador.
    Chequea si el dict del jugador esta vacío.
    '''
    if jugador is not None:
        mostrar_jugador_nombre_posicion(jugador)
        for key, cantidad in jugador["estadisticas"].items():
            mensaje = "{0} - {1}".format(key,cantidad)
            print(mensaje)

def mostrar_estadisticas_por_indice(lista:list,indice:int)->dict:
    '''
    Recibe una lista y un int
    Confirma que no este vacía y que el indice pertenezca a la lista
    '''
    if len(lista) > 0 and indice-1 <= len(lista):
        jugador = lista[indice-1]
        mostrar_estadisticas_jugador(jugador)
        return jugador

def ingresar_indice_jugador(lista:list)->int:
    '''
    Recibe una lista.
    Muestra los jugadores de la lista y le pide al usuario que ingrese un número.
    Retorna el numero seleccionado si esta entre 0 y 12 o -1 si no cumple con la condición.
    '''
    mostrar_lista_jugadores_indice(lista)
    opcion_seleccionada = input("\nIngrese el indice del jugador que desea ver sus datos: ") 
    if opcion_seleccionada.isdigit() and int(opcion_seleccionada) <= len(lista) and int(opcion_seleccionada) > 0:
        return int(opcion_seleccionada) 
    else:
        print("\nERROR: Ingrese un número entre 1 y 12\n")
        return -1
    
def magic_team_mostrar_estadistica_por_indice(lista:list)->dict:
    '''
    Recibe una lista
    Comprueba que no este vacía, imprime los jugadores y sus indices. Le pide al usuario que ingrese por consola un indice.
    Comprueba que el número ingresado sea correcto e imprime las estadisticas del jugador que represente el jugador.
    '''
    if len(lista) > 0:
        numero_indice = -1
        while numero_indice == -1:
            numero_indice = ingresar_indice_jugador(lista)
            if numero_indice > 0:
                jugador_retorno = mostrar_estadisticas_por_indice(lista,numero_indice)
                return jugador_retorno

def generar_csv(nombre_archivo:str, jugador:dict):
    '''
    Recibe un str y un jugador.
    Genera un csv con el jugador pasado por parámetro y lo guarda con sus datos (nombre, posicion, estadísticas).
    '''
    lista_claves = ["nombre","posicion"]
    lista_claves += list(jugador["estadisticas"].keys())
    cabecera = ",".join(lista_claves)
    with open(nombre_archivo, "w+") as archivo:
        archivo.write(cabecera + "\n")
        lista_valor = [jugador["nombre"],jugador["posicion"]]
        for valor in jugador["estadisticas"].values():
            lista_valor.append(str(valor))
        dato = ",".join(lista_valor) + "\n"
        archivo.write(dato)

def ingresar_nombre_usuario()->str:
    opcion_seleccionada = input("\nIngrese el nombre del jugador que desea ver sus logros: ") 
    if re.match(r'[a-zA-Z]',opcion_seleccionada):
        return str(opcion_seleccionada) 
    else:
        print("\nERROR: Ingrese un nombre con letras de la a a la z, sin simbolos ni números\n")
        return -1

def buscar_jugador_por_nombre(nombre:str,lista:list)->list:
    '''
    Recibe un str y una lista.
    Recorre la lista y devuelve una lista con los jugadores que coincidan con el nombre ingresado.
    '''
    if nombre != -1 and len(lista) > 0:
        lista_retorno = []
        for jugador in lista:
            jugador_retorno = None
            jugador_retorno = re.findall(nombre.upper(),jugador["nombre"].upper())
            if jugador_retorno != []:
                lista_retorno.append(jugador)
        return lista_retorno
    else:
        print("ERROR!: Vacía la lista o el nombre pasado por parámetro a la función 'buscar_jugador_por_nombre'")
        return []

def mostrar_logros_jugador (jugador:dict):
    '''
    Recibe un jugador.
    Printea los logros del jugador.
    '''
    if jugador is not None:
        for logro in jugador["logros"]:
            print (logro)

def magic_team_mostrar_logros_por_nombre(lista:list):
    if len(lista) > 0:
        nombre = ingresar_nombre_usuario()
        jugador_encontrado = buscar_jugador_por_nombre(nombre,lista)
        if jugador_encontrado != []:
            for jugador in jugador_encontrado:
                mostrar_jugador_nombre_posicion(jugador)
                mostrar_logros_jugador(jugador)

def obtener_dato (jugador:dict,dato:str)->float:
    '''
    Recibe un dict y un str.
    Recorre las estadisticas buscando la clave pasada por dato y devuelve el valor de la misma.
    '''
    if jugador is not None:
        for key, valor in jugador["estadisticas"].items():
            if dato == key:
                return valor

def sumar_dato(lista:list,dato:str):
    '''
    Recibe una lista y un str del tipo de dato que se quiera.
    Recorre la lista y retorna la sumatoria del dato pasado por parámetro.
    '''
    if len(lista) > 0:
        dato_retorno = 0
        for jugador in lista:
            dato_retorno += obtener_dato(jugador,dato)
        return dato_retorno

def obtener_promedio(lista:list,dato:str):
    '''
    Recibe lista y dato tipo str
    Suma el dato solicitado y de toda la lista y devuelve el promedio
    '''
    if len(lista) > 0:
        suma_total = sumar_dato(lista,dato)
        promedio = suma_total / (len(lista))
        return promedio
    else:
        print("ERROR!: Lista vacía o dato solicitado equivocado")
        return -1

def ordenar_por_dato(lista:list,dato:str,flag_orden:bool)->list:
    '''
    Recibe lista, dato tipo str y un booleano
    Metodo quiksort, devuelve la lista ordenada segun el orden pedido
    '''
    lista_der = []
    lista_izq = []
    if(len(lista)<=1):
        return lista
    else:
        pivot = lista[0]
        if flag_orden:
            for elemento in lista[1:]:
                if(obtener_dato(elemento,dato)) < (obtener_dato(pivot,dato)):
                    lista_der.append(elemento)
                else:
                    lista_izq.append(elemento)
        else:
            for elemento in lista[1:]:
                if(obtener_dato(elemento,dato)) > (obtener_dato(pivot,dato)):
                    lista_der.append(elemento)
                else:
                    lista_izq.append(elemento)
    lista_izq = ordenar_por_dato(lista_izq,dato,flag_orden)
    lista_izq.append(pivot) 
    lista_der = ordenar_por_dato(lista_der,dato,flag_orden)
    lista_izq.extend(lista_der) 
    return lista_izq

def magic_team_mostrar_promedios_puntos_por_partidos(lista:list):
    '''
    Recibe una lista
    Devuelve la lista ordenada por puntos y printea los jugadores ordenados por partidos
    '''
    if len(lista) > 0:
        dato = "promedio_puntos_por_partido"
        promedio = obtener_promedio(lista,dato)
        lista_ordenada = (ordenar_por_dato(lista,dato,True))
        print("\nEl promedio de puntos por partido total de los jugadores es: {0}\n".format(promedio))
        mostrar_lista_jugadores_nombre_dato(lista_ordenada,dato)
    else:
        print("ERROR!: Lista vacía")

def devolver_jugador_pertenece_salon_fama(jugador:dict)->bool:
    '''
    Recibe un diccionario
    Devuelve True si el jugador pertenece al salon de fama
    '''
    for dato in jugador["logros"]:
        if dato == "Miembro del Salon de la Fama del Baloncesto":
            return True
    return False

def magic_team_mostrar_si_jugador_pertenece_salon_fama(lista:list):
    '''
    Recibe una lista
    Pide al usuario que ingrese un usuario y printea si pertenece al salon de la fama o no
    '''
    if len(lista) > 0:
        nombre = ingresar_nombre_usuario()
        jugador_encontrado = buscar_jugador_por_nombre(nombre,lista)
        if jugador_encontrado != []:
            for jugador in jugador_encontrado:
                if devolver_jugador_pertenece_salon_fama(jugador):
                    print("El jugador {0} pertenece al salon de fama".format(jugador["nombre"]))
                else:
                    print("El jugador {0} no pertenece al salon de fama".format(jugador["nombre"]))

def obtener_jugador_mayor_dato(lista:list,dato:str)->dict:
    '''
    
    '''
    if len(lista) > 0:
        jugador_mayor = lista[0]
        for jugador in lista[1:]:
            if obtener_dato(jugador,dato) > obtener_dato(jugador_mayor,dato):
                jugador_mayor = jugador
        return jugador_mayor
    
# ------------------------------------------------------- ------------------------------------------------------- ------------------------------------------------------- -------------------------------------------------------   
def obtener_jugador_con_mas_logros(lista:list)->dict:
    '''
    
    '''
    if len(lista) > 0:
        jugador_mayor = lista[0]
        for jugador in lista[1:]:
            if obtener_cantidad_logros(jugador) > obtener_cantidad_logros(jugador_mayor):
                jugador_mayor = jugador
        return jugador_mayor
    
def magic_team_mostrar_jugador_con_mas_logros(lista:list):
    if len(lista) > 0:
        jugador_mayor = obtener_jugador_con_mas_logros(lista)
        mostrar_jugador_nombre_posicion(jugador_mayor)

def magic_team_mostrar_jugador_mayor_cantidad_dato(lista:list,dato:str):
    if len(lista) > 0:
        jugador_mayor = obtener_jugador_mayor_dato(lista,dato)
        mostrar_jugador_nombre_dato(jugador_mayor,dato)
    
def obtener_lista_mayor_valor(lista:list,valor:int,dato:str)->list:
    '''
    
    '''
    if len(lista) > 0:
        lista_aux = ordenar_por_dato(lista,dato,True)
        lista_retorno = []
        for jugador in lista_aux:
            if obtener_dato(jugador,dato) > valor:
                lista_retorno.append(jugador)
            else:
                break
        if len(lista_retorno) > 0:
            return lista_retorno
        else:
            print("No hay jugadores con mas de {0} {1}".format(valor,dato))
            return []

def ingresar_numero():
    '''
    Recibe una lista.
    Muestra los jugadores de la lista y le pide al usuario que ingrese un número.
    Retorna el numero seleccionado.
    '''
    numero_ingresado = input("\nIngrese un número: ") 
    if numero_ingresado.isdigit():
        return int(numero_ingresado)
    else:
        print("\nERROR: Ingrese un número\n")
        return -1

def magic_team_mostrar_jugadores_mayor_dato_segun_input(lista:list,dato:str):
    '''
    Recibe una lista y un dato tipo str
    Le pide al user que ingrese un número. La funcion mostrara todos los jugadores que superen en sus estadisticas
    el numero escrito por el usuario.
    '''
    if len(lista) > 0:
        while True:
            numero_ingresado = ingresar_numero()
            lista_mayores_dato = obtener_lista_mayor_valor(lista,numero_ingresado,dato)
            if len(lista_mayores_dato) > 0:
                mostrar_lista_jugadores_nombre_dato(lista_mayores_dato,dato)
                break
            else:
                print("\nReintentelo\n")

def eliminar_ultimo_jugador_lista(lista:list)->list:
    '''
    Recibe una lista
    Elimina el último elemento de la lista
    '''
    if len(lista) > 0:
        lista_retorno = lista[0:-1]
        return lista_retorno
    else:
        print("No hay jugadores en la lista")

def eliminar_ultimo_jugador_de_la_lista_por_dato(lista:list,dato:str)->dict:
    '''
    Recibe una lista y un dato
    Ordena la lista segun el dato y elimina el último dict de la lista
    '''
    if len(lista) > 0:
        lista_aux = ordenar_por_dato(lista,dato,True)
        lista_aux = eliminar_ultimo_jugador_lista(lista_aux)
        return lista_aux

def obtener_promedio_sin_peor_jugador(lista:list,dato:str)->float:
    '''
    Recibe una lista y un dato
    Ordena la lista segun el dato, elimina el último elemeno y calcula el promedio de la lista
    '''
    if len(lista) > 0:
        lista_aux = eliminar_ultimo_jugador_de_la_lista_por_dato(lista,dato)
        return obtener_promedio (lista_aux,dato)
    else:
        print("No hay jugadores en la lista")

def obtener_cantidad_logros(jugador:dict)->int:
    '''
    
    '''
    if jugador is not None:
        cantidad_logros = len(jugador["logros"])
        return cantidad_logros

def obtener_jugadores_por_posicion(lista:list)->dict:
    '''
    Recibe una lista
    Recorre la lista generando un diccionario con las claves que buscamos y en los valores el nombre de los elementos que comparten esta particularidad (ej: color de ojos, pelo, etc)
    Retorna el diccionario creado
    '''
    diccionario_retorno = {}
    for jugador in lista:
        posicion_jugador = jugador["posicion"]
        if posicion_jugador in diccionario_retorno:
            diccionario_retorno[posicion_jugador].append(jugador) #XQ el append no se pinta en amarillo? no lo reconoce al escribir pero si funciona
        else:
            diccionario_retorno[posicion_jugador] = [jugador]
    return diccionario_retorno

def mostrar_jugadores_por_posicion(jugadores_ordenados:dict):
    '''
    
    '''
    for valor in jugadores_ordenados.values():
        mostrar_lista_jugadores_nombre_posicion(valor)

def magic_team_mostrar_jugadores_ordenados_por_input_y_posicion(lista:list,dato:str):
    if len(lista) > 0:
        while True:
            numero_ingresado = ingresar_numero()
            lista_mayores_dato = obtener_lista_mayor_valor(lista,numero_ingresado,dato)
            if len(lista_mayores_dato) > 0:
                jugadores_mayores_posicion = obtener_jugadores_por_posicion(lista_mayores_dato)
                mostrar_jugadores_por_posicion(jugadores_mayores_posicion)
                break
            else:
                print("\nReintentelo\n")

# ------------------------------------------/ PRUEBAS /------------------------------------------/ PRUEBAS /------------------------------------------/ PRUEBAS /------------------------------------------/
# ------------------------------------------/ PRUEBAS /------------------------------------------/ PRUEBAS /------------------------------------------/ PRUEBAS /------------------------------------------/

lista_jugadores = leer_archivo(path)
# mostrar_lista_jugadores_indice(lista_jugadores)
# mostrar_lista_jugadores_indice(lista_jugadores)
# indice_seleccionado = (ingresar_indice_jugador(lista_jugadores))
# mostrar_estadisticas_por_indice(lista_jugadores,indice_seleccionado)
# magic_team_mostrar_estadistica_por_indice(lista_jugadores)
# generar_csv("NombrePrueba.csv",lista_jugadores[0])
# mostrar_logros_jugador(lista_jugadores[0])
# nombre_buscar = ingresar_nombre_usuario()
# print(buscar_jugador_por_nombre(nombre_buscar,lista_jugadores))
# magic_team_mostrar_logros_por_nombre(lista_jugadores)
# print(sumar_dato(lista_jugadores,"temporadas"))
# print(ordenar_por_dato(lista_jugadores,"temporadas",True))
# mostrar_lista_jugadores_nombre_dato(ordenar_por_dato(lista_jugadores,"promedio_puntos_por_partido",True),"promedio_puntos_por_partido")
# magic_team_mostrar_promedios_puntos_por_partidos(lista_jugadores)
# print(devolver_jugador_pertenece_salon_fama(lista_jugadores[0]))
# magic_team_mostrar_si_jugador_pertenece_salon_fama(lista_jugadores)
# mostrar_jugador_nombre_dato(obtener_jugador_mayor_dato(lista_jugadores,"bloqueos_totales"),"bloqueos_totales")
# mostrar_jugador_mayor_cantidad_rebotes_totales(lista_jugadores)
# mostrar_jugador_mayor_porcentaje_tiros_de_campo(lista_jugadores)
# # print(obtener_lista_mayor_valor(lista_jugadores,60,"porcentaje_tiros_de_campo"))
# magic_team_mostrar_jugadores_mayor_dato_segun_input(lista_jugadores,"porcentaje_tiros_de_campo")
# lista_aux = eliminar_ultimo_jugador_lista(lista_jugadores)
# lista_aux = eliminar_ultimo_jugador_de_la_lista_por_dato(lista_jugadores,"promedio_puntos_por_partido")
# magic_team_mostrar_jugadores_mayor_dato_segun_input(lista_aux,"porcentaje_tiros_de_campo")
# mostrar_lista_jugadores_nombre_dato(lista_aux,"promedio_puntos_por_partido")
# print(magic_team_menu_principal())
# print(obtener_cantidad_logros(lista_jugadores[1]))
# magic_team_mostrar_jugador_con_mas_logros(lista_jugadores)
# mostrar_jugadores_por_posicion(obtener_jugadores_por_posicion(lista_jugadores))
# magic_team_mostrar_jugadores_ordenados_por_input_y_posicion(lista_jugadores,"porcentaje_tiros_de_campo")