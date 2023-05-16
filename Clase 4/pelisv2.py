from flask import Flask
import random
app = Flask(__name__)

bootstrap = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'

nav = """
<ul class="nav nav-tabs" style="background: silver;">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
</ul>

"""


peliculas={
    "1000":{ "Nombre":"El padrino", "Director":"Francis Ford Coppola","Estreno":1972},
    "1001":{ "Nombre":"Senderos de gloria", "Director":"Stanley Kubrick","Estreno":1957},
    "1002":{ "Nombre":"La naranja mecanica", "Director":"Stanley Kubrick","Estreno":1971},
    "1003":{ "Nombre":"La ventana indiscreta", "Director":"Alfred Hitchcock","Estreno":1954},
    "1004":{ "Nombre":"Psicosis", "Director":"Alfred Hitchcock","Estreno":1960},
    "1005":{ "Nombre":"Taxi driver", "Director":"Martin Scorsese","Estreno":1976}
}

def componente_peli(movies):
    acumula = ""
    for id, peli in movies.items():
        acumula += f"""        
            <h1><a href="/pelicula/{id}">{peli["Nombre"]}</a></h1>
            <h2>{peli["Director"]}</h2>
            <p> {peli["Estreno"]}</p>        
            <hr>                
            """  
    return acumula


def home(peliculas):
    peli = f"""
            <html>
                <title> Listado Peliculas </title>
                {bootstrap}
                {nav}
                {componente_peli(peliculas)}                
            """
    return peli

@app.route("/")
def peliculas_www():
    return home(peliculas)


@app.route('/pelicula/<string:peli_id>')
def movie(peli_id):    
    return (f"""  <html><title> Listado Peliculas </title>{bootstrap}
        <h1>{peliculas[peli_id]["Nombre"]}</h1>
        <h2>{peliculas[peli_id]["Director"]}</h2>
        <p> {peliculas[peli_id]["Estreno"]}</p>
        <p><a href="/" class="btn btn-lg btn-primary">Regresar a la home</a></p>
        </html>
        """)

app.run("localhost",8080)

#Versión 2 de peliculas