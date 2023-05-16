import random
class Chatbot():
    def __init__(self):
        self.mensajes =["Bienvenido","Hola","En que puedo ayudarlo","Un gusto verlo aqui"]
    
    def saludar(self):
        saludo = random.choice(self.mensajes)
        return saludo

class Chatbotdelivery(Chatbot):
    def __init__(self):
        super().__init__()
        self.listapalabras = ["cena","almuerzo","comida","comer"]
        self.listadopedidos = ["Puedo ofrecerle una pizza","Puedo ofrecerle una Milapizza"]
    def responder(self):
        a=input("Ingrese su pedido: ")
        c= ""
        for x in a.split(" "):
            if x in self.listapalabras:
                c=random.choice(self.listadopedidos)
            else:
                c = "Aguarde un momento un representante se contactara a la brevedad"
        return c

class Chatbotbanco(Chatbot):    
    def bienvenida(self,edad):
        self.edad = edad
        if self.edad >= 18:
            return "Aguarde, un representante lo atendera a la brevedad"
        else:
            return "Se requiere la presencia de un mayor de 18 anios"

chat = Chatbot()
print(chat.saludar())

deli = Chatbotdelivery()
print(deli.responder())

ban = Chatbotbanco()
edad =int(input("Ingrese su edad: "))
print(ban.bienvenida(edad))