

def average_temps(temps):
    sum_of_temps = 0

    for tem in temps:
        sum_of_temps += float(tem)
    
    return sum_of_temps / len(temps)


def run():
    temps = [21, 24, 24, 22, 20, 23, 24]

    average = average_temps(temps)
    print('La temperatura promedio de la semana es: {}'.format(round(average,2)))


if __name__ == '__main__':
    run()