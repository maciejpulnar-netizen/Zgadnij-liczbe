import random
import string

def generuj_haslo(dlugosc=20):
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = ''.join(random.choice(znaki) for i in range(dlugosc))
    return haslo

print('--- GENERATOR HASEL ---')
dl = int(input('Jak dlugie ma byc haslo? '))
ile = int(input('Ile hasel chcesz wygenerowac? '))

print(f' --- Twoje bezpieczne hasla o dlugosci {dl} ---')
for i in range(ile):
    print(f'{i+1}. {generuj_haslo(dl)}')
print(f"Wygenerowano pomyslnie {ile} hasel o dlugości {dl} znakow")