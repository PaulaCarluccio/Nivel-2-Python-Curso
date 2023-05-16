class Cyborg:
    bateria = 100
    encendido = True
    lenguaje = "en"

print(Cyborg.bateria)
Cyborg.bateria = 90
print(Cyborg.bateria)
if(Cyborg.encendido):
    if(Cyborg.lenguaje == "es"):
        print("Encendido")
    else:
        print("Turn on")
else:
    if(Cyborg.lenguaje == "es"):
        print("Apagado")
    else:
        print("Turn off")    
