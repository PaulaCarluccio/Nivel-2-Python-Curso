try:  
  print(mivar)
  2/0
except NameError as e:
  print("Variable no definida: " + str(e))
except:
  print("Escenario inesperado")