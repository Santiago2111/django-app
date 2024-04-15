import requests
import os

def get_commet_data(api_key):
    print("::: COMETS INFORMATION :::")
    api_url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

#Main
api_key_nasa = ""
get_commet_data(api_key_nasa)