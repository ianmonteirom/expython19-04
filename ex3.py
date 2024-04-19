"""
3. Faça um programa que exiba todos os números primos menores que 1 milhão.
"""

for n in range(2, 1000000+1):
    cont_divs = 0
    for d in range(1, n):
        if n % d == 0:
            cont_divs += 1
    if cont_divs < 2:
        print(f'{n} é primo')
