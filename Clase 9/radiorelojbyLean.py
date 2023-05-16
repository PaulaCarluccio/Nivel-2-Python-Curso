from datetime import datetime
class Reloj():
    def __init__(self):
        super(Reloj,self).__init__()
        self.fecha = datetime.now()
        self.horas = int(self.fecha.strftime('%H'))
        self.minutos = int(self.fecha.strftime('%M'))
        self.segundos = int(self.fecha.strftime('%S'))
        
    def Mostrarhora(self):
        self.horaactual  = self.fecha.strftime('%H:%M:%S')
        return self.horaactual

class Radio():
    def __init__(self):
        #super(Radio,self).__init__()
        self.am = [580,850]
        self.fm = [88,108]

# hereda de reloj y radio, memoriza 2 AM y 2 FM, luego las guarda en un list por banda.
class Radioreloj(Reloj,Radio):
    def memorizar(self):
        self.estacionesam = []
        self.estacionesfm = []
#guarda am 
        while len(self.estacionesam) <2:
            self.estacion = int(input("ingese estacion AM: "))
            if int(self.estacion) in range(self.am[0],self.am[1]) and  int(self.estacion) not in self.estacionesam:
                self.estacionesam.append(int(self.estacion))
            else:
                print("Ingrese una estacion AM valida entre 580 y 850 (No es valido repetir la estacion)")
#guarda fm
        while len(self.estacionesfm) <2:
            self.estacion = int(input("ingese estacion FM: "))
            if int(self.estacion) in range(self.fm[0],self.fm[1]) and  int(self.estacion) not in self.estacionesfm:
                self.estacionesfm.append(int(self.estacion))
            else:
                print("Ingrese una estacion FM valida entre 88 y 108 (No es valido repetir la estacion)")
# muestra las radios AM y FM memorizadas. 
    def alarma(self):
        self.estacioselecc = 0 
        print("Selecione Estacion de Radio")
        self.radioss= "\n"
        for x in self.estacionesfm:
            self.radioss +=f"{x} FM \n"  
        for x in self.estacionesam:
            self.radioss +=f"{x} AM \n"
        print(self.radioss)
# pide seleccionar y guarda la estacion de radio de entre las memorizadas   
        while self.estacioselecc == 0:
            self.b = int(input("Seleccione radio para alarma de las guardadas(solo numero): "))
            if self.b in  self.estacionesam:
                self.estacioselecc =str(self.b) + " AM"
            elif self.b in self.estacionesfm:
                self.estacioselecc =str(self.b) + " FM"
            else:
                print("Radio no encontrada en memorizadas, intente nuevamente")
#pide y valida la hora de la alarma     
        ala = True
        while ala:
            self.alarma=input("ingrese hora de la alarma HH:MM (formato 24 HS): ")
            if ":" in self.alarma:
                self.a=self.alarma.split(":")
                if (int(self.a[0])) >=0 and (int(self.a[0])) < 24 and (int(self.a[1])) >= 0 and (int(self.a[1])) <60:     
                    self.horaalarma =str(self.a[0]) +":"+ str(self.a[1]) +"Hs"
                    ala = False
                else:
                    print("Formato de fecha y hora no valido.")
            else:
                print("Formato de fecha y hora no valido.")
        
        return self.horaalarma

#instancio 
h = Radioreloj()
print(h.Mostrarhora())
h.memorizar()
h.alarma()
print(f"Se establece la alarma a la hora {h.horaalarma} y se establecio la Radio en {h.estacioselecc}")
#Ejemplo by Lean