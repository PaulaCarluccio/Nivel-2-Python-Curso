peliculas= {
  "1000" : {
    "titulo" : "Inception",
    "year" : 2010,
    "actor" : "DiCaprio"
  },
  "1001" : {
    "titulo" : "Interstellar",
    "year" : 2014,
    "actor" : "McConaughey"
  },
  "1002" : {
    "titulo" : "Memento",
    "year" : 2000,
    "actor" : "Pearce"
  }  
}


ordenado = tuple(sorted(peliculas, key=lambda x: (peliculas[x]['year']), reverse=False))
print(ordenado)

for i in ordenado:
    print(f"{i}: {peliculas[i]['titulo']} ({peliculas[i]['year']}) - Protagonista: {peliculas[i]['actor']}")