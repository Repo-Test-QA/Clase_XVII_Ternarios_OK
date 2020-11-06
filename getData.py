import json
import requests

class GetData:
    def get(self, end_point):
        #Voy a traer la baseurl más la otra parte (parámetro end_point determina el pokemon)
        #para completar el endpoint
        with open('data.json') as json_file:
            data = json.load(json_file)
            #Seria ideal que los requests esten fuera de los casos de pruebas y esten en otro lado.
            needed_data = requests.get(data['base_url'] + end_point)
            return needed_data

    #Así como en el método de arriba recupero parte del request, del endpoint
    #Acá vamos a recuperar la información de cada pokemon que consultemos, desde
    #luego tenemos que tener por cada pokemo su archivo .json con su información
    def get_pokemon_data(self, pokemon):
        with open(pokemon + '.json') as poke:
            return json.load(poke)






