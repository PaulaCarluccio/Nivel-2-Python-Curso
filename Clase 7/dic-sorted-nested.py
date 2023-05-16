peliculas= {
  "1000" : {
    "titulo" : "Inception",
    "year" : 2010
  },
  "1001" : {
    "titulo" : "Interstellar",
    "year" : 2014
  },
  "1002" : {
    "titulo" : "Time Machine",
    "year" : 1960
  },  
  "1003" : {
    "titulo" : "Planet of the apes",
    "year" : 1968
  }   
}

ordenados = sorted(peliculas, key=lambda x: (peliculas[x]['year']),reverse=False)
print(ordenados)

for i in ordenados:
  print(peliculas[i]["titulo"])
  print(peliculas[i]["year"])
  print("**********")