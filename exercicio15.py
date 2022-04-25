# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 
#por dia e R$0,15 por Km rodado.

km = float(input('Quantos KM percorridos ? '))
day = int(input('Quantos Dias alugados ? ')) 

valueKm = km * 0.15 
valueDay = day * 60 

print('O total a pagar é : R${:.2f}'.format(valueKm+valueDay))
