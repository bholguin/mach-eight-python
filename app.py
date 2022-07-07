import requests


def search_players(valor_usuario: int) -> None:
    try:
        players = requests.get("https://mach-eight.uc.r.appspot.com/")
        data = players.json()  
        izq = (len(data['values']) - 1)
        der = (len(data['values']) - 1)
        while der != 0:
            izq = izq -1
            if izq >= 0:
                sum = (int(data['values'][der]["h_in"])+int(data['values'][izq]["h_in"]))
                if sum == int(valor_usuario):
                    print("{0} - {1} inch + {2} - {3} inch = {4}".format(data['values'][der]["first_name"], data['values'][der]["h_in"], data['values'][izq]["first_name"], data['values'][izq]["h_in"],  int(data['values'][der]["h_in"]) +  int(data['values'][izq]["h_in"])))
                    print("--------------------------------------------")
            else: 
                der = der-1
                izq = der
    except:
        print("Ocurrio un error con la data del api")


valor_usuario =  input("por favor ingrese un numero ")
valor_int = 0

try:
    valor_int = int(valor_usuario)
    search_players(valor_int)
except:
    print("debe ingresar un numero")



    
        

    


