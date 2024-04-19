"""
5. Faça um programa que gera um número aleatório de 1 a 100. O usuário deve tentar
acertar qual o número foi gerado. A cada tentativa o programa deverá informar se o
número gerado é maior ou menor que o chute do usuário. O programa acaba quando o
usuário acertar o número gerado. Ao final, o programa deve informar em quantas
tentativas o número foi descoberto
"""

from random import randint

num_random = randint(1, 100)
tents = 1

chute = int(input('Pensei em um número. Tente acertar qual número eu chutei de 1 a 100: '))
while chute != num_random:
    tents += 1
    print(f'Você errou! {chute} é', end='')
    if chute < num_random:
        print(' MENOR do que meu número.')
    elif chute > num_random:
        print(' MAIOR do que meu número.')
    chute = int(input('Tente novamente: '))

if chute == num_random:
    print('--' * 24)
    print(f'Você acertou! Meu número era {num_random}!\n'
          f'Número de tentativas: {tents}')
    print('--' * 24)
