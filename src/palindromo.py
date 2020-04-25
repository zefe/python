
def palindromo(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        print('Si es un palindromo')
        print(reversed_word)
    else:
        print('No es un palindromo')

def run():
    word = str(input('Ingreasa una palabra:  '))
    palindromo(word)


if __name__ == '__main__':
    run()