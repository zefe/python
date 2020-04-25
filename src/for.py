
def run():
    for i in range(20):
        print('Hello {}'.format(i))
    
    for i in range(30):
        if i % 3 == 0:
            print(i**2)
        elif 1 == 22:
            break
    for i in range(30):
        if i % 3 == 0:
            print(i)
        elif i == 22:
            break
    # string - str

    r = 'Ferrocarril'

    for letter in r:
        print(letter)

if __name__ == '__main__':
    run()