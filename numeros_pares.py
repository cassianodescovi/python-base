"""
Faça um programa que imprime os números pares de 1 a 200

ex

`python3 numeros_pares.py`
2
4
6
8
...
"""

lista = []
numeros = list(range(1,201))

for numero in numeros:
    if numero % 2 == 0:
        lista.append(numero)
print(lista)
    