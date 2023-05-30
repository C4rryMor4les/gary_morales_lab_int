from django.shortcuts import render

# Create your views here.
def owner_list(request):
    # data_context ={
    #         'nombre': 'Katty Paredes',
    #         'edad': 16,
    #         'dni': 42425656,
    #         'pais': 'Peru',
    #         'vigente': False
    # },
    data_context = [
        {
            'nombre': 'Katty Paredes',
            'edad' : 16,
            'dni' : 42425656,
            'pais' : 'Peru',
            'vigente' : False,
            'pokemons':[
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques':['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard' ]
                }
            ]
        },
        {
            'nombre': 'Miguel Valera',
            'edad': 26,
            'dni': 43454545,
            'pais': 'España',
            'vigente': False,
            'pokemons': [
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques': ['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard']
                }
            ]
        },
        {
            'nombre': 'Jesus de la Cruz',
            'edad': 30,
            'dni': 44444545,
            'pais': 'Colombia',
            'vigente': False,
            'pokemons': [
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques': ['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard']
                }
            ]
        },
        {
            'nombre': 'Liliana Vargas',
            'edad': 24,
            'dni': 454546436,
            'pais': 'España',
            'vigente': True,
            'pokemons': [
                {
                    'nombre_pokemon': 'Charizard',
                    'ataques': ['Ataque 1 - Charizard', 'Ataque 2 - Charizard', 'Ataque 3 - Charizard']
                }
            ]
        }
    ]
    return render(request,'owner/owner_list.html',context={'data':data_context})
