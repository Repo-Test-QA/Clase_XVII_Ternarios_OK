#Para trabajar con nuestros casos de pruebas
import unittest
#Importamos la base url
from getData import GetData


class TestPokemon(unittest.TestCase):
    def test_search_valid_pokemon(self):
        # Get, se realiza sobre una URL, utilizamos un endpoint para recuperar su información
        #pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
        # Cambiamos por el endpoint Kakuna

        #Vamos a llamar al método que tiene nuestra url base, le vamos a pasar como parámetro
        #el pokemon que vamos a querer de endpoint para traer su información
        #Creamos el objeto de la clase getData
        my_data = GetData()
        pokemon = my_data.get('kakuna')
        my_pokemon = pokemon.json()

        #pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/kakuna')
        #my_pokemon = pokemon.json()

        #Verificamos el código del estado
        #print(pokemon.status_code)
        #Va a devolver la infomación del endpoint (pokemon/pikachu) en formato json
        #print(my_pokemon)
        #Quiero que solo me devuelva la información de la propiedad weight
        #print(my_pokemon['weight'])
        # Quiero recuperar la información de los movimientos (tiene 5) del pokemon kakuna
        #print(my_pokemon['moves'])
        # Estamos verificando el movimiento en el índice 4
        #print(my_pokemon['moves'][4])


        #Me voy a traer la información que se encuentra en el archivo kakuna.json
        #por tanto, ya no voy a utilizar la lista moves que se muestra abajo.
        #Para ello voy a importar la librería json
        #with open('kakuna.json') as kakuna:
        #    data = json.load(kakuna)

        #Comentamos lo de arriba, ahora vamos a recuperar la información del pokemon a consultar
        data = my_data.get_pokemon_data('kakuna')

        #Ahora en una variable voy a asignar los 5 movimientos del pokemon Kakuna
        #moves = ['string-shot', 'harden', 'iron-defense', 'bug-bite', 'electroweb']


        #Ahora quiero saber si 200 es el valor que devolvio el request cuyo valor es 200, es decir si esta OK
        self.assertEqual(200, pokemon.status_code)
        #Pikachu, quiero verificar que 60 sea el valor de la propiedad => weight cuyo valor es 60
        #kakuna, quiero verificar que 100 sea el valor de la propiedad => weight cuyo valor es 100
        #self.assertEqual(100, my_pokemon['weight'])
        self.assertEqual(data['weight'], my_pokemon['weight'])

        #Va a recorrer todos los elementos de los movimientos
        for i in my_pokemon['moves']:
            #Ahora si se puede recorrer el array, porque i es un elemento del array porque esta iterando
            print(i['move']['name'])
            #Vamos a verificar que los elementos que recorra de la lista my_pokemon['moves]
            #si se encuentran también en la lista de elementos de moves
            #self.assertTrue(i['move']['name'] in moves)
            self.assertTrue(i['move']['name'] in data['moves'])


            #Ahora lo que se tiene como respuesta de nuestra solicitud del get,
            #y esa respuesta en formato json, lo vamos a tener en otro archivo porque se
            #esta repitiendo ese código, creamos el archivo getData
            #todos mis llamados a la API van a usar esa URL, derrpenete en uno de mis
            #ambientes, por tanto lo debemos tener en otro archivo data.json


    def test_search_pokemon_by_number(self):
        #pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/1')
        my_data = GetData()
        pokemon = my_data.get('1')

        # Comentamos lo de arribaa, ahora vamos a recuperar la información del pokemon a consultar
        data = my_data.get_pokemon_data('bulbasaur')

        my_pokemon = pokemon.json()

        self.assertEqual(200, pokemon.status_code)
        self.assertEqual(my_pokemon['name'], data['name'])

        #Creamos un archivo kakuna.json porque queremos los datos del pokemos kakuna






