# Divisas

def run():
    print('C A L C U L A D O R A D E D I V I S A S')
    print('Convietr de pesos mexicanos a pesos colombianos')
    print('')

    amount = float(input('Ingreasa la cantidad de pesos mexicanos:  '))

    result = foreing_exchange_calculator(amount)

    print('${} pesos mexicanos  son ${} pesos colombianos'.format(amount, result))
    print('')


def foreing_exchange_calculator(amount):
    mex_to_col_rate = 145.95
    return mex_to_col_rate * amount


if __name__ == '__main__':
    run()