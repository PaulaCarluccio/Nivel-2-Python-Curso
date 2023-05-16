from flask import Flask
import colores
import menu
app = Flask(__name__)


titulo = "Mi Mejor Flask"

bootstrap = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'

def mostrarmenu():
    acumula = f"""<ul class="nav" style="background:{colores.paleta2["background"]}">"""
    for clave, valor in menu.menu1.items():
        acumula += f"""<li class="nav-item"><a class="nav-link" href="{valor}">{clave}</a><li>"""
    return acumula + '</ul>'

def home():
    homelibro = f"""
            <html>
                {bootstrap}                
                {mostrarmenu()}    
                <title>{titulo}</title>

            </html>	
                            
            """
    return homelibro


@app.route("/")
def home_www():
	return home()


app.run("localhost",8080)