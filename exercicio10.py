# Crie um programa que leia quando dinheiro uma pessoa tem na carteira e mostre quantos dolares equivale esse valor.

real = float(input('Digite o valor que você tem em sua carteira : R$'))

valorDolar = 4.67
resul = real / valorDolar

print('O valor de R$ {:.2f} em dolar é US {:.2f}'.format(real, resul))
