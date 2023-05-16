class Robot:
    def __init__(self):
        self.bateria = 50
        self.encendido = True
    def encender(self):
        if self.encendido == False:
            self.encendido = True
            return "Mensaje: se ha encencido con éxito"
        else:
            return "Mensaje: el robot ya estaba encendido"
            self.encendido = False
    def apagar(self):
        if self.encendido:
            self.encendido = False
            return "Mensaje: se ha apagado con éxito"
        else:
            return "Mensaje: el robot ya estaba apagado"    
            self.encendido = True


mirobot = Robot()
print(mirobot.encender())
print(mirobot.apagar())
print(mirobot.encender())
