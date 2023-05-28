import parcial_programacion_1h
import dream_team_menu

path = "C:/Users/dcris/Desktop/UTN/Laboratorio2023/Ejercicios/Ejercicios/data_dream_team.json"
lista_jugadores = parcial_programacion_1h.leer_archivo(path)

dream_team_menu.dream_team_app(lista_jugadores)