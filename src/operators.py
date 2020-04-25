

def operations():
    print('Say nino or senor')
    print('')

    age = int(input('Cuantos años tienes?  '))

    calculate_saludo(age)

def calculate_saludo(age):
    if age > 18:
        print('Hello senor')
    else:
        print('Hello nino')

if __name__ == '__main__':
    operations()