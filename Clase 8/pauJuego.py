#Objeto Juego (Padre)
    #Props que recibe = reglas(str), year(int)
    #Método tiempoenstock.
#Clase juego de mesa (Juego)
    #Props que recibe cantidad de jugadores(int) / fichas(int)
    #Método mostrar reglas,lanzamiento, tiempo en stock, jugadores y fichas
#Clase videogame (Juego)
    #Consolas (lista)
    #Método mostrar: reglas,year y lista de consolas
import datetime

class Juego:
    def __init__(self, reglas, year):
        self.reglas = reglas
        self.year = year
        self.x = datetime.datetime.now()
        self.hoy = self.x.year
    def tiempoenstock(self):
        tiempo = self.hoy - self.year
        return tiempo

    
class JuegoDeMesa(Juego):
    def __init__(self, reglas, year, cantjugadores, fichas):
        super().__init__(reglas, year)
        self.cantjugadores = cantjugadores
        self.fichas = fichas
    def mostrartod(self):
        data = "Han pasado " + str(super().tiempoenstock()) + " años desde su creación en " + str(self.year) + ". Las reglas son: " + self.reglas + "y se juega de a " + str(self.cantjugadores) + " con " + str(self.fichas)
        return data
class VideoGame(Juego):
    def __init__(self, reglas, year, consolas):
        super().__init__(reglas, year)
        self.consolas = consolas
        
    def listarconsolas(self):
        acumula = ""
        for x in self.consolas:
            acumula = acumula + str(x) + ","
        return acumula
    
    def mostrartodo(self):
        data = "Han pasado " + str(super().tiempoenstock()) + " años desde su lanzamiento en " + str(self.year) + self.reglas + " Actualmente está presente en " + self.listarconsolas() + "."
        return data
        
ludo_reglas = "La regla principal es no lanzar el dado hacia el tablero, el jugador puede lanzar el 6 todas las veces que desee, sin perder su turno."
ludo_creacion = 1896
overwatch_reglas = "Overwatch es un variopinto shooter por equipos que cuenta con un diverso reparto de poderosos héroes, combates 6 contra 6."
overwatch_consolas = ["Windows PC", "PlayStation 4", "XOne"]
overwatch_lanzamiento = 2016

ludo = JuegoDeMesa(ludo_reglas, ludo_creacion, 4, 4)
print(ludo.mostrartod())

over = VideoGame(overwatch_reglas, overwatch_lanzamiento, overwatch_consolas)
print(over.mostrartodo())    