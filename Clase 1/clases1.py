class Robot:
    bateria = 50
    encendido = False
    def encender(self):
        encendido = True
        return "Mensaje: se ha encencido con éxito"
    def apagar(self):
        encendido = False
        return "Mensaje: se ha apagado con éxito"
    def mostrarBateria(self):
        return "Estado de carga: " + str(self.bateria) + "%"
    def cargarBateria(self):
        self.bateria+=1
        return "Estado de carga: " + str(self.bateria) + "%"        

print(Robot.bateria)
mirobot = Robot()
print(mirobot.mostrarBateria())
print(mirobot.cargarBateria())
Robot.bateria = Robot.bateria+1
print(Robot.bateria)
