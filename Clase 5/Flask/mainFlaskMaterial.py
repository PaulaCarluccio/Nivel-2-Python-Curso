from flask import Flask

app = Flask(__name__)


titulo = "Mi Mejor Flask"

material = """

<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
<script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>

"""

def mostrarmenu():    
    return (f"""
    
<button id="demo-menu-lower-left"
        class="mdl-button mdl-js-button mdl-button--icon">
         <i class="material-icons">more_vert</i>
</button>

<ul class="mdl-menu mdl-menu--bottom-left mdl-js-menu mdl-js-ripple-effect"
    for="demo-menu-lower-left">
  <li class="mdl-menu__item">Home</li>
  <li class="mdl-menu__item mdl-menu__item--full-bleed-divider">Libros</li>
  <li class="mdl-menu__item">Autores</li>
  <li class="mdl-menu__item"><a href="/otra">Ver Otra</a></li>
  <li class="mdl-menu__item"><a href="https://getmdl.io/started/index.html" target="_blank">Link a la librería</a></li>
</ul>

    """)

def home():
    homelibro = f"""
            <html>
                {material}                
                {mostrarmenu()}    
                <title>{titulo}</title>

            </html>	
                            
            """
    return homelibro


@app.route("/")
def home_www():
	return home()

@app.route("/otra")
def otra_www():
	return(f"""
<body>
{material}   
<div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
  <header class="mdl-layout__header">
    <div class="mdl-layout__header-row">
      <!-- Title -->
      <span class="mdl-layout-title">Title</span>
    </div>
    <!-- Tabs -->
    <div class="mdl-layout__tab-bar mdl-js-ripple-effect">
      <a href="#scroll-tab-1" class="mdl-layout__tab is-active">Primer Tab</a>
      <a href="#scroll-tab-2" class="mdl-layout__tab">Tab 2</a>
      <a href="#scroll-tab-3" class="mdl-layout__tab">Tab 3</a>
      <a href="#scroll-tab-4" class="mdl-layout__tab">Tab 4</a>
      <a href="#scroll-tab-5" class="mdl-layout__tab">Tab 5</a>
      <a href="#scroll-tab-6" class="mdl-layout__tab">Tab 6</a>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
  </div>
  <main class="mdl-layout__content">
    <section class="mdl-layout__tab-panel is-active" id="scroll-tab-1">
      <div class="page-content">
      
        Soy el gran texto 1
      </div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-2">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-3">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-4">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-5">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-6">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
  </main>
</div>
</body>    
    """) 


app.run("localhost",8080)