import requests
import os

def get_data():
    os.system("clear")  # Clear the screen
    print("::: INFORMACIÓN DEL SISTEMA SOLAR :::")
    
    while True:
        print("::: MENÚ :::")
        print("[1]. Planetas")
        print("[2]. Lunas")
        print("[3]. Estrellas")
        print("[4]. Asteroides")
        print("[5]. Cometas")
        print("[6]. Salir")
        
        opt = input("Elija una opción: ")
        
        if opt == "1":
            api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
            response = requests.get(api_url)
            data = response.json()
            
            print("\n::: Planetas :::")
            for body in data["bodies"]:
                if body["bodyType"] == "Planet":
                    print(f"Nombre: {body['englishName']}")
                    print(f"Gravedad: {body['gravity']}")
                    print(f"Inclinación: {body['inclination']}")
                    print(f"Es Planeta: {body['isPlanet']}")
                    print()

        elif opt == "2":
            api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
            response = requests.get(api_url)
            data = response.json()

            print("\n::: Lunas :::")
            for body in data["bodies"]:
                if body["bodyType"] == "Moon":
                    print(f"Nombre: {body['englishName']}")
                    print(f"Gravedad: {body['gravity']}")
                    print(f"Inclinación: {body['inclination']}")
                    print(f"Es Planeta: {body['isPlanet']}")
                    print()

        elif opt == "3":
            api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
            response = requests.get(api_url)
            data = response.json()
    
            print("\n::: Estrellas :::")
            for body in data["bodies"]:
                if body["bodyType"] == "Star": 
                    print(f"Nombre: {body['englishName']}")
                    print(f"Gravedad: {body['gravity']}")
                    print(f"Inclinación: {body['inclination']}")
                    print(f"Es Planeta: {body['isPlanet']}")
                    print()

        elif opt == "4":
            api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
            response = requests.get(api_url)
            data = response.json()
    
            print("\n::: Asteroides :::")
            for body in data["bodies"]:
                if body["bodyType"] == "Asteroid":
                    print(f"Nombre: {body['englishName']}")
                    print(f"Gravedad: {body['gravity']}")
                    print(f"Inclinación: {body['inclination']}")
                    print(f"Es Planeta: {body['isPlanet']}")
                    print()

        elif opt == "5":
            api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
            response = requests.get(api_url)
            data = response.json()
    
            print("\n::: Cometas :::")
            for body in data["bodies"]:
                if body["bodyType"] == "Comet":
                    print(f"Nombre: {body['englishName']}")
                    print(f"Gravedad: {body['gravity']}")
                    print(f"Inclinación: {body['inclination']}")
                    print(f"Es Planeta: {body['isPlanet']}")
                    print()

        elif opt == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no valida. Intente otra vez")
get_data()