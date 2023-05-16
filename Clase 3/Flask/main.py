from flask import Flask
import random
app = Flask(__name__)
titulo = "Mi sitio"
nombres1= ["Dami","Pau","Nico","Valen"]
nombres2= ["Mati","Martin","Male"]
numeros = [10,50,1,2,5,11,4]

def cabecera(titulo,subtitulo):
    return (f"""
    <header>
        <h1>{titulo}</h1>
        <h2>{subtitulo}</h2>
    </header>
    """
    )

def listarnombres(nombres):        
    acumula = "<ul>"
    for nombre in nombres:        
	    acumula += "<li>"+str(nombre) + "</li>"
    return acumula + "</ul>"  

def listarimpares(lista):
    acumula = cabecera("Impares","Mis grandes números impares")
    acumula += "<ul>"
    for numero in numeros: 
        if numero%2 != 0:      
	        acumula += "<li>"+str(numero) + "</li>"
    return acumula + "</ul>"

def listarpares(lista):
    acumula = cabecera("Pares","Mis mejores números pares")
    acumula += "<ul>"
    for numero in numeros: 
        if numero%2 == 0:      
	        acumula += "<li>"+str(numero) + "</li>"
    return acumula + "</ul>"
    

@app.route("/")
def home_www():
	return (f"""
    <html>
        <title>{titulo}</title>
        <h1>Hola Mundo</h1>
        <ul>
            <li><a href="/pares">Pares</a></li>
            <li><a href="/impares">Impares</a></li>
            <li><a href="/otra">Otra</a></li>
        </ul>
    </html>    
    """)

@app.route("/pares")
def pares_www():
	return listarpares(numeros)

@app.route("/impares")
def impares_www():
	return listarimpares(numeros)

@app.route("/nombres")
def nombres_www():
    return listarnombres(nombres2)

@app.route("/otra")
def otra():
	return (f"""
<!DOCTYPE html>
<html>
    <title>El titulo de la pestaña - {titulo}</title>
    <h1>Hola</h1>
    <div style="width:400px;height:400px;background:red;">
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequatur modi labore nesciunt libero vero eligendi, odit dolorem suscipit id? Amet maxime nulla officia animi excepturi tenetur eius ipsa, accusantium id?</p>
    </div>
    {listarnombres(nombres1)}
    <p><a href="https://google.com">Google</a></p>
    <p><a href="02.html">Ir a página 2</a></p>
</html>

""")

app.run("localhost",8080)
#app.run("0.0.0",8080)