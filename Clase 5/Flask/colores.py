paleta1 = {
  "background": "lightblue",
  "color1": "black",
  "color2": "brown",
  "colorlink": "red"
}

paleta2 = {
  "background": "silver",
  "color1": "navy",
  "color2": "white",
  "colorlink": "green"
}

class Link():
    def __init__(self,color,background):        
        self.color = color
        self.background = background
    def crearLink(self,link,texto):        
        return (f"""<a href="{link}" style="color:{self.color};background:{self.background}">{texto}</a>""")