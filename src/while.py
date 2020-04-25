import random

def encontrar_numero(num):
    number_found = False
    random_number = random.randint(0, num)

    while not number_found:
            number = int(input('Intenta un numero:  '))

            if number == random_number:
                print('Felicidades Entyraste el nuemoro')
                number_found = True
            elif number > random_number:
                print('El numero es mas pequeño')
            else:
                print('El numero es mas grande')

def run():
    print('EN CUENTRA EL NUMERO EN EL RANGO QUE TU DECES')
    print('')
    num = int(input('Ingresa el numero deseado:  '))

    encontrar_numero(num)


if __name__ == '__main__':
    run()