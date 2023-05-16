import datetime
class Cyborg():
    bateria = 100
    encendido = False
    mensaje = "Hola"
    def saludar(self):
        mensaje = self.mensaje
        print(mensaje)

for elemento, valor in Cyborg.__dict__.items():
    print (f"{elemento} : {valor} - {type(valor)}")
print("***********")
for elemento, valor in Cyborg.__dict__.items():
    if elemento == "mensaje":
        print (f"{valor}")
print("***********")
for elemento, valor in datetime.__dict__.items():
    if not elemento.startswith('__') and not str(valor).startswith('<function'):
        print (f"{elemento} : {valor}")
print("***********")
for elemento, valor in datetime.__dict__.items():
    if not elemento.startswith('__') and not str(valor).startswith('<function'):
        print (f"{elemento} : {valor}")