import requests
import os

def get_data():
    os.system("clear")  # Clear the screen
    print(":: SOLAR SYSTEM INFORMATION")
    
    while True:
        print("#### MAIN MENU ####")
        print("[1]. Planets")
        print("[2]. Moons")
        print("[3]. Stars")
        print("[4]. Asteroids")
        print("[5]. Comets")
        print("[6]. Exit")
        
        option = input("Press an option: ")
        
        if option == "1":
            get_planets()
        elif option == "2":
            get_moons()
        elif option == "3":
            get_stars()
        elif option == "4":
            get_asteroids()
        elif option == "5":
            get_comets()
        elif option == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

def get_planets():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(api_url)
    data = response.json()

    print("\n#### Planets ####")
    for body in data["bodies"]:
        if body["bodyType"] == "Planet":
            print(f"English name: {body['englishName']}")
            print(f"Gravity: {body['gravity']}")
            print(f"Inclination: {body['inclination']}")
            print(f"Body type: {body['bodyType']}")
            print()

def get_moons():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(api_url)
    data = response.json()

    print("\n#### Moons ####")
    for body in data["bodies"]:
        if body["bodyType"] == "Moon":
            print(f"English name: {body['englishName']}")
            print(f"Gravity: {body['gravity']}")
            print(f"Inclination: {body['inclination']}")
            print(f"Body type: {body['bodyType']}")
            print()

def get_stars():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(api_url)
    data = response.json()
    
    print("\n#### Stars ####")
    for body in data["bodies"]:
        if body["bodyType"] == "Star": 
            print(f"English name: {body['englishName']}")
            print(f"Gravity: {body['gravity']}")
            print(f"Inclination: {body['inclination']}")
            print(f"Body type: {body['bodyType']}")
            print()

def get_asteroids():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(api_url)
    data = response.json()
    
    print("\n#### Asteroids ####")
    for body in data["bodies"]:
        if body["bodyType"] == "Asteroid":
            print(f"English name: {body['englishName']}")
            print(f"Gravity: {body['gravity']}")
            print(f"Inclination: {body['inclination']}")
            print(f"Body type: {body['bodyType']}")
            print()

def get_comets():
    api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(api_url)
    data = response.json()
    
    print("\n#### Comets ####")
    for body in data["bodies"]:
        if body["bodyType"] == "Comet":
            print(f"English name: {body['englishName']}")
            print(f"Gravity: {body['gravity']}")
            print(f"Inclination: {body['inclination']}")
            print(f"Body type: {body['bodyType']}")
            print()
get_data()