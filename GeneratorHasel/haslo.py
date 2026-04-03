import random
import string

def generuj_haslo(dlugosc=12):
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = ''.join(random.choice(znaki) for i in range(dlugosc))
    return haslo

print('--- GENERATOR HASIEL ---')
dl = int(input('Jak dlugie ma byc haslo? '))
print(f'Twoje bezpieczne haslo to: {generuj_haslo(dl)}')
