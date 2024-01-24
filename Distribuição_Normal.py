''' Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue 
uma distribuição aproximadamente normal, com média 1,70 e desvio padrão de 0,1. 
Com estas informações obtenha o seguinte conjunto de probabilidades:

A. probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.

B. probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.

C. probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros. '''

from scipy.stats import norm

media = 1.70
desvio_p = 0.1

# Letra A - Calculando z para 1.80m

z = (1.80 - media) / desvio_p
print(z)
print(20 * '----')
# Calculando a probabilidade dentro da área correspondente as alturas abaixo de 1.80

prob_menor = norm.cdf(z)
print(f'A probabilidade de uma pessoa do grupo ter menos de 1.80m é de {prob_menor:.5f}.')
print(20 * '----')
# Calculando a probabilidade de uma pessoa selecionada ao acaso, ter entre 1.60 à 1.80m
#Calculando o z inferior

z_inf = (1.60 - media) / desvio_p
print(f'O Z inferior é {z_inf}.')
print(20 * '----')
#Calculando o z superior
z_sup = (1.80 - media) / desvio_p
print(f'O Z Superior é {z_sup}.')
print(20 * '----')
prob_B = norm.cdf(z_sup) - norm._cdf(z_inf)
print(f'A probabilidade de uma pessoa ter de 1.60m à 1.80m é de {prob_B:.5f}.')

print(20 * '----')

# A probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1.90m 
z_2 = (1.90 - media) / desvio_p

print(z_2)
print(20 * '----')

prob_maior = norm.cdf(z_2)
print(f'A probabilidade de uma pessoa ser selecionada ao acaso e ter mais 1.90m é de {prob_maior:.5f}. ')
print(20 * '----')