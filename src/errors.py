countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 40,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(input('Ingresa tu pais: ')).lower()
    try:
        print('La población de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de {}'.format(country))
