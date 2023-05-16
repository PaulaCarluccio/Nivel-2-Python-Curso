import colores
from menu import menu1
print(colores.paleta1["background"])

miLink = colores.Link("red","yellow")
print(miLink.crearLink("https://damiandeluca.com.ar","Dami Web Site"))

for clave, valor in menu1.items():
  print(f"""
   <a href="{valor}">{clave}</a>
   """)  