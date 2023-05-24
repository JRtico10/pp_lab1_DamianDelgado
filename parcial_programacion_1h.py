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

path = "C:/Users/dcris/Desktop/UTN/Laboratorio2023/Ejercicios/Ejercicios/data_dream_team.json"

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
        #Recorrer el dict .item()?.
        mostrar_jugador_nombre_posicion(jugador)
        for key, cantidad in jugador["estadisticas"].items():
            mensaje = "{0} - {1}".format(key,cantidad)
            print(mensaje)

def mostrar_estadisticas_por_indice(lista:list,indice:int):
    if len(lista) > 0 and indice-1 <= len(lista):
        jugador = lista[indice-1]
        mostrar_estadisticas_jugador(jugador)

def ingresar_indice_jugador()->int:
    '''
    
    '''
    pass
# ------------------------------------------/ PRUEBAS /------------------------------------------/ PRUEBAS /------------------------------------------/ PRUEBAS /------------------------------------------/
# ------------------------------------------/ PRUEBAS /------------------------------------------/ PRUEBAS /------------------------------------------/ PRUEBAS /------------------------------------------/

lista_jugadores = leer_archivo(path)
# mostrar_lista_jugadores_indice(lista_jugadores)
mostrar_lista_jugadores_indice(lista_jugadores)
mostrar_estadisticas_por_indice(lista_jugadores,9)
