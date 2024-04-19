"""
1. Faça um programa que some todos os números inteiros positivos abaixo de 1000 que
são múltiplos de 3 ou 5.
"""

soma = 0

for i in range(999, 0, -1):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f'Resultado da soma: {soma}')
