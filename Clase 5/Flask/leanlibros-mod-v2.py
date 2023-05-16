from flask import Flask
import random


libros={
    "1000":{ "Nombre":"Catedrales", "Autor":"Claudia Pinieiro","Editorial":"Alfaguara","Edicion":2020,"Paginas":390,"Genero":"Policial","tapa":"https://via.placeholder.com/300.png/111/fff"},
    "1001":{ "Nombre":"1984", "Autor":"Orwell George","Editorial":"Debolsillo","Edicion":2013,"Paginas":352,"Genero":"Fantasia","tapa":"https://via.placeholder.com/300.png/11f/09f"},
    "1002":{ "Nombre":"Largo Petalo de Mar", "Autor":"Isabel Allende","Editorial":"Sudamericana","Edicion":2019,"Paginas":384,"Genero":"Narrativa","tapa":"https://via.placeholder.com/300.png/091/f2f"},
    "1003":{ "Nombre":"La cucaracha", "Autor":"Mcewan Ian","Editorial":"Anagrama","Edicion":2020,"Paginas":126,"Genero":"Narrativa","tapa":"https://via.placeholder.com/300.png/09f/fff"},
    "1004":{ "Nombre":"La madre de frankenstein", "Autor":"Grandes Almudena","Editorial":"Tusquets","Edicion":2020,"Paginas":780,"Genero":"Narrativa","tapa":"https://via.placeholder.com/300.png/022/2ff"},
    "1005":{ "Nombre":"Harry Potter y el prisionero de Askaban", "Autor":"Rowling J.K.","Editorial":"Salamandra","Edicion":2019,"Paginas":384,"Genero":"Fantasia","tapa":"https://via.placeholder.com/300.png/033/3ff"},
    "1006":{ "Nombre":"El Hombre en busca de sentido", "Autor":"Frankl Viktor E.","Editorial":"Herder","Edicion":2016,"Paginas":160,"Genero":"Psicologia","tapa":"https://via.placeholder.com/300.png/033/33f"},
    "1007":{ "Nombre":"Homo Deus", "Autor":"Harari Yuval Noah","Editorial":"Debate","Edicion":2016,"Paginas":496,"Genero":"Fisica","tapa":"https://via.placeholder.com/300.png/09f/fff"},
    "1008":{ "Nombre":"Letramania la imprenta mayuscula", "Autor":"Gomez Carrillo Sara Ines, Johnson Sally","Editorial":"Kel","Edicion":2001,"Paginas":68,"Genero":"Educacion","tapa":"https://via.placeholder.com/300.png/044/44f"},
    "1009":{ "Nombre":"Harry Potter y la piedra filosofal (SLYTHERIN)", "Autor":"Rowling J.K.","Editorial":"Salamandra","Edicion":2018,"Paginas":320,"Genero":"Fantasia","tapa":"https://via.placeholder.com/300.png/045/55f"},
    "1010":{ "Nombre":"Harry Potter y la piedra filosofal (GYFFINDOR)", "Autor":"Rowling J.K.","Editorial":"Salamandra","Edicion":2018,"Paginas":320,"Genero":"Fantasia","tapa":"https://via.placeholder.com/300.png/69f/1ff"},
    "1011":{ "Nombre":"Harry Potter y la piedra filosofal (HUFFLEPUFF)", "Autor":"Rowling J.K.","Editorial":"Salamandra","Edicion":2018,"Paginas":320,"Genero":"Fantasia","tapa":"https://via.placeholder.com/300.png/111/222"},
    "1012":{ "Nombre":"Harry Potter y la piedra filosofal (RAVENCLAW)", "Autor":"Rowling J.K.","Editorial":"Salamandra","Edicion":2018,"Paginas":320,"Genero":"Fantasia","tapa":"https://via.placeholder.com/300.png/312/132"},
    "1013":{ "Nombre":"La Casa de los Espiritus", "Autor":"Isabel Allende","Editorial":"Plaza & Janes Editores","Edicion":2011,"Paginas":560,"Genero":"Narrativa","tapa":"https://via.placeholder.com/300.png/09f/fff"},
    "1014":{ "Nombre":"Mas alla del Invierno", "Autor":"Isabel Allende","Editorial":"Plaza & Janes Editores","Edicion":2017,"Paginas":352,"Genero":"Narrativa","tapa":"https://via.placeholder.com/300.png/99f/eff"},

}
app = Flask(__name__)

class Libros:
    
    def __init__(self):
        
        self.bootstrap = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'
        
        self.nav = '''
        <ul class="nav nav-tabs">
        <li class="nav-item">
            <a class="nav-link" href="/">Home</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/recomendado">Recomendado</a>
        </li>
         <li class="nav-item">
            <a class="nav-link" href="/autores">Autores</a>
        </li>
        </ul>

        '''
# Muestra en el index el listado de libros con nombre autor y genero
    def componente_libro(self,libros):
        libro = f"""
                <html>
                    <title> Listado libros </title>
                    {self.bootstrap}
                    {self.nav}              
                """
        for id, lib in libros.items():
            libro += f"""        
                <h2><a href="/libro/{id}">{lib["Nombre"]}</a></h2>
                <h4>Autor: {lib["Autor"]}</h4>
                <p>Genero: {lib["Genero"]}</p>        
                <hr>                
                """  
        return libro

######################################################################
# saca de el diccionario libros el listado de Autores
    def lista_aut(self,libros):
        lista_autores=[]
        for id, values in libros.items():
            if libros[id]["Autor"] not in lista_autores:
                lista_autores.append(libros[id]["Autor"])
        return lista_autores
#################################################################
# Muestra el listado de autores en '/autores'
    def autores(self,lista):
        autores=f"""
                <html> 
                    <title> Listado Autores </title> 
                    {self.bootstrap} 
                    {self.nav} 
                    <ul>
                    """
        for autor in lista:
            autores += f"""
                <li><a href='/autores/{autor}'>{autor}</a></li>
                """              
        return autores + '</ul></html>'

####################################################################
#Libros de autores
    def autoreslibros(self,autores_id):
        librosdeautor = f"  <html><title>Listado Libros</title>  {self.nav} {self.bootstrap}"
        for libro_id, values in libros.items():
            if autores_id == libros[libro_id]["Autor"]:
                librosdeautor += f"""
        <h3>Nombre:{libros[libro_id]["Nombre"]}</h3>
        <h4>Autor: {libros[libro_id]["Autor"]}</h4>
        <p>Edicion: {libros[libro_id]["Edicion"]}</p>
        <p>Paginas: {libros[libro_id]["Paginas"]}</p>
        <p>Genero: {libros[libro_id]["Genero"]}</p>        
        """
        return librosdeautor + '</html>'

###########################################################
#Plantilla HTML libro
def librosingle(libro_id,objeto,page):
    return (f"""  
        <html>
        <title> Listado Libros </title>  
        {objeto.nav} 
        {objeto.bootstrap}
        <h1>{page}</h1>
        <img src="{libros[libro_id]["tapa"]}" style="float:left; width:200px;margin:10px;">
        <h4>Nombre:{libros[libro_id]["Nombre"]}</h4>        
        <h6>Autor: {libros[libro_id]["Autor"]}</h6>
        <p>Edicion: {libros[libro_id]["Edicion"]}</p>
        <p>Paginas: {libros[libro_id]["Paginas"]}</p>
        <p>Genero: {libros[libro_id]["Genero"]}</p>
        </html>
        """)

#Flask
@app.route("/")
def libros_www():
    objeto=Libros()
    return objeto.componente_libro(libros)

@app.route("/recomendado")
def recomendado_www():
    objeto=Libros()
    libro_id=random.choice(list(libros.keys()))
    return librosingle(libro_id,objeto,"Libro recomendado")

@app.route('/libro/<string:libro_id>')
def libro(libro_id):
    objeto=Libros()
    return librosingle(libro_id,objeto,"Ficha del libro")

@app.route("/autores")
def autores_www():
    objeto=Libros()
    return objeto.autores(objeto.lista_aut(libros))

@app.route('/autores/<string:autores_id>')
def libros_autores(autores_id):
    objeto=Libros()
    return objeto.autoreslibros(autores_id)

app.run("localhost",8080)

    #Versión modificada en clase  -  basada en el ejercicio de Leandro