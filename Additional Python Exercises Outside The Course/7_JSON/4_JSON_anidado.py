#`json.load()`, `json.dump()`, `json.loads()`, `json.dumps()`.
#4. Cree un programa que lea un JSON anidado (una lista de equipos, cada uno con una lista de jugadores) y muestre todos los jugadores.


import json

with open("teams.json","r") as file:
    teams = json.load(file)
    for team in teams:
        print(f"Equipo: {team['nombre']}")
        for player in team["jugadores"]:
            print(f"Jugador: {player['nombre']} - Posición: {player['posición']}")

            