class Parrafo(object):
    def __init__(self, texto):        
        self.texto = texto
    def mostrarP(self):        
        return (f"""<p>{self.texto}</p>""")


class Link(Parrafo):
    def __init__(self,texto,link):
        Parrafo.__init__(self,texto)        
        self.link = link
    def mostrarLink(self):        
        return (f"""<p><a href="{self.link}">{self.texto}</a></p>""")        

parrafin = Parrafo("Mi texto")
print(parrafin.mostrarP())

milink = Link("Mi link","https://damiandeluca.com.ar")
print(milink.mostrarP())
print(milink.mostrarLink())