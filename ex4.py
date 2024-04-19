"""
4. Faça um programa que some todos os números primos existentes entre a e b, onde a e
b são números informados pelo usuário.
"""

a = int(input('Valor de A: '))
b = int(input('Valor de B: '))
soma = 0

for n in range(a, b+1):
    cont_divs = 0
    if n == 0 or n == 1:
        continue
    for d in range(a, b+1):
        if n % d == 0:
            cont_divs += 1
    if cont_divs <= 2:
        print(f'{n} é primo')
