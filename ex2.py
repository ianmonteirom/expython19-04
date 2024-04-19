"""
2. Um funcionário foi contratado em 2015 com um salário de R$ 2000,00. Em 2016 ele
recebeu um aumento de 1.5%. A partir de 2017, os aumentos sempre correspondem ao
dobro da porcentagem do ano anterior. Faça um algoritmo que determine o salário do
funcionário no ano de 2024.
"""

sal_2015 = 2000
sal_2016 = 2000 + (2000 * 1.5 / 100)
porc = 1.5
print(f'Salário de 2016: {sal_2016}')

for i in range(2017, 2025):
    porc *= 2
    salario = 2000 + (2000 * porc / 100)
    print(f'Salário de {i}: {salario}')

