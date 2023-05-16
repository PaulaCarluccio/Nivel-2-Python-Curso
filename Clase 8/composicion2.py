class Wifi:
    def enviar(self, mensaje):
        self.tiempo = "100ms"
        return f"Enviado {mensaje} x WIFI (tiempo: {self.tiempo})"


class Mobile4G:
    def enviar(self, mensaje):
        self.tiempo = "120ms"
        self.latencia = "20ms"
        return f"Enviado {mensaje} x 4G  (tiempo: {self.tiempo} - latencia {self.latencia})"


class Mensajero:
    # Definición de composición: usar objetos dentro de otros
    conectividad = Wifi()

    def elegirconexion(self, conectividad):
        self.conectividad = conectividad        

    def envioUsr(self, mensaje):
        print(self.conectividad.enviar(mensaje))


client = Mensajero()
client.envioUsr("Hola ¿Vemos Series?")

client.elegirconexion(Mobile4G())
client.envioUsr("Hola ¿Sale Running?")