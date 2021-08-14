import re
from collections import Counter

def vogais(string):
    return Counter(re.sub('[^aeiouAEIOU]', '', string))

def consoantes(string):
    return Counter(re.sub('[^bcdfghjklmnpqrstvxywzBCDFGJKLMNPQRSTVWXZ]', '', string))

palavra = "paralelepipedo"

print('A palavra', palavra ,'tem', len(palavra), 'letras.')

for letra in palavra:
    print(letra)

print(vogais(palavra))

print(consoantes(palavra))
