def dividir(x, y): 
     
    try: 
        r = x / y
        print("Resultado :", r) 

    except ZeroDivisionError: 

        print("Error: división x cero")
    except: 

        print("Otro problema")        
dividir(3,0)