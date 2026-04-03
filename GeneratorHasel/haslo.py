import random
import string

def generuj_haslo(dlugosc=12):
    znaki = string.ascii_letters + string.punctuation
    haslo = ''.join(random.choice(znaki) for i in range(dlugosc))
    return haslo

print('--- GENERATOR 5 HASIEL ---')
dl = int(input('Jak dlugie ma byc haslo? '))
for i in range(5):
    print(f'{i+1}. {generuj_haslo(dl)}')
