import re
import dream_team_funciones

def imprimir_menu_Dream_Team()->None:
    print("\nMenu de opciones\n"
                        "1- Mostrar todos los jugadores del Dream Team\n2- Mostrar estadísticas de un jugador por índice\n"
                        "3- Guardar las estadísticas del jugador seleccionado\n4- Buscar un jugador por su nombre y mostrar sus logros\n"
                        "5- Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team\n6- Buscar un jugador por su nombre y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto\n"
                        "7- Mostrar el jugador con la mayor cantidad de rebotes totales\n8- Mostrar el jugador con el mayor porcentaje de tiros de campo\n"
                        "9- Mostrar el jugador con la mayor cantidad de asistencias totales\n10- Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor\n"
                        "11- Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valo\n12- Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor\n"
                        "13- Mostrar el jugador con la mayor cantidad de robos totales\n14- Mostrar el jugador con la mayor cantidad de bloqueos totales\n"
                        "15- Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor\n16- Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido\n"
                        "17- Mostrar el jugador con la mayor cantidad de logros obtenidos\n18- Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor\n"
                        "19- Mostrar el jugador con la mayor cantidad de temporadas jugadas\n20- Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor\n"
                        "23- Last Dance\n\n0- Salir del programa\n")

def magic_team_menu_principal():
    imprimir_menu_Dream_Team()
    opcion_seleccionada = input("\nIngrese la opción que desea: ")
    if re.match(r'([0-9]|1[0-9]|20|23)', opcion_seleccionada): #VER EL REGEX DE NUMEROS
        return int(opcion_seleccionada)
    else:
        print("Opción inválida!")
    return -1

def dream_team_app(lista:list):
    flag_tercera_opcion = False
    while True:
        # parcial_programacion_1h.clear_console()
        respuesta_int = magic_team_menu_principal()
        match respuesta_int:
            case 1:
                dream_team_funciones.mostrar_lista_jugadores_nombre_posicion(lista)
                pass
            case 2:
                flag_tercera_opcion = True
                jugador_aux = dream_team_funciones.magic_team_mostrar_estadistica_por_indice(lista)
                pass
            case 3:
                if flag_tercera_opcion:
                    dream_team_funciones.generar_csv("data_jugador_{0}.csv".format(jugador_aux["nombre"]),jugador_aux)
                else:
                    print("Primero debe ingresar al punto dos")
            case 4:
                dream_team_funciones.magic_team_mostrar_logros_por_nombre(lista)
                pass
            case 5:
                dream_team_funciones.magic_team_mostrar_promedios_puntos_por_partidos(lista)
                pass
            case 6:
                dream_team_funciones.magic_team_mostrar_si_jugador_pertenece_salon_fama(lista)
                pass
            case 7:
                dream_team_funciones.magic_team_mostrar_jugador_mayor_cantidad_dato(lista,"rebotes_totales")
                pass
            case 8:
                dream_team_funciones.magic_team_mostrar_jugador_mayor_cantidad_dato(lista,"porcentaje_tiros_de_campo")
                pass
            case 9:
                dream_team_funciones.magic_team_mostrar_jugador_mayor_cantidad_dato(lista,"asistencias_totales")
                pass
            case 10:
                dream_team_funciones.magic_team_mostrar_jugadores_mayor_dato_segun_input(lista,"promedio_puntos_por_partido")
                pass
            case 11:
                dream_team_funciones.magic_team_mostrar_jugadores_mayor_dato_segun_input(lista,"promedio_rebotes_por_partido")
                pass
            case 12:
                dream_team_funciones.magic_team_mostrar_jugadores_mayor_dato_segun_input(lista,"promedio_asistencias_por_partido")
                pass
            case 13:
                dream_team_funciones.magic_team_mostrar_jugador_mayor_cantidad_dato(lista,"robos_totales")                
                pass
            case 14:
                dream_team_funciones.magic_team_mostrar_jugador_mayor_cantidad_dato(lista,"bloqueos_totales")                
                pass
            case 15:
                dream_team_funciones.magic_team_mostrar_jugadores_mayor_dato_segun_input(lista,"porcentaje_tiros_libres")
                pass
            case 16:
                promedio_sin_peor_jugador = dream_team_funciones.obtener_promedio_sin_peor_jugador(lista,"promedio_puntos_por_partido")
                print("\nEl promedio de puntos por partido sin el peor jugador es de: {0}\n".format(promedio_sin_peor_jugador))
                pass
            case 17:
                dream_team_funciones.magic_team_mostrar_jugador_con_mas_logros(lista)
                pass
            case 18:
                dream_team_funciones.magic_team_mostrar_jugadores_mayor_dato_segun_input(lista,"porcentaje_tiros_triples")
                pass
            case 19:
                dream_team_funciones.magic_team_mostrar_jugador_mayor_cantidad_dato(lista,"temporadas")                
                pass
            case 20:
                dream_team_funciones.magic_team_mostrar_jugadores_ordenados_por_input_y_posicion(lista,"porcentaje_tiros_de_campo")
                pass
            case 23:
                pass
            case 0:
                print("Gracias por usar el programa")
                break
